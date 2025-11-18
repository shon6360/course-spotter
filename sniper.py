import requests, time, atexit, os

# important stuff
MY_DISCORD_USER = os.getenv("MY_DISCORD_USER")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
ALL_COURSES_URL = "https://classes.rutgers.edu/soc/api/courses.json"
ALL_OPEN_SECTIONS_URL = "https://classes.rutgers.edu/soc/api/openSections.json"
WEBREG_URL = "https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas"

# Helpers
def notify_discord(msg):
	'''
	Essentially our output stream which is sent to my discord, 'msg' is a string
	'''
	global DISCORD_WEBHOOK
	requests.post(DISCORD_WEBHOOK, json={"content": msg}, timeout=10)

def cleanup():
	'''
	Make sure the program exits are well documented
	'''
	notify_discord("Sniper disabled")

# core functionality
def request(url, params):
	try:
		response = requests.get(url, params=params)
		response.raise_for_status()  # Raise an error for bad responses
		return response.json()

	except requests.exceptions.RequestException as e:
		notify_discord("Error: "+e)
		return None

def get_indexes(all_courses, course_strings):
	'''
	Search for each course in the list 'courses' in 'all_courses' by 'courseString'
	return a list of all the indexes
	'''
	indexes = []
	for course in all_courses:
		if course["courseString"] in course_strings:
			for section in course["sections"]:
				indexes.append({"index": section["index"], "courseString": course["courseString"], "expandedTitle" : course["expandedTitle"], "meetingTimes" : section["meetingTimes"]})
	return indexes


def main():
	atexit.register(cleanup)
	
	params = {
		"year": "2026",
		"term": "1",
		"campus": "NB"
	}
	users_and_course_strings = {
		MY_DISCORD_USER : ["01:198:213", "01:198:336", "01:198:440", "01:198:428"]
	}
	users_and_indexes = {}
	
	all_courses = request(ALL_COURSES_URL, params)
	
	for user in users_and_course_strings:
		users_and_indexes[user] = get_indexes(all_courses, users_and_course_strings[user]);
	notify_discord("Sniper enabled")
	while True:
		all_open_sections = request(ALL_OPEN_SECTIONS_URL, params);		
		for user in users_and_indexes:
			for index in users_and_indexes[user]: # this is a linear search, needs to be replaced with binary search or something
				if(index in all_open_sections):
					notify_discord("hello");
	
	time.sleep(60)

main();
