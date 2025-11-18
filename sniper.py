import requests, time, atexit, sys

# important links
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1438576405490307122/SFSjV9tXIZMqL5dVKceg7hJYGfzhRgplky_DJW8wyHKzuGw7j2gLSJo_HocPp7y5A4Ie"
ALL_COURSES_URL = "https://classes.rutgers.edu/soc/api/courses.json"
ALL_OPEN_SECTIONS_URL = "https://classes.rutgers.edu/soc/api/openSections.json"
WEBREG_URL = "https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas"

# Helpers
def notify_discord(msg):
	'''
	Essentially our output stream, 'msg' is a string
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

def get_indexes(all_courses, course_titles):
	'''
	Search for each course in the list 'courses' in 'all_courses' by 'courseString'
	return a list of all the indexes
	'''
	indexes = []
	for course in all_courses:
		if course["courseString"] in course_titles:
			for section in course["sections"]:
				indexes.append(section["index"])
	return indexes


def main():
	atexit.register(cleanup)
	
	params = {
		"year": "2026",
		"term": "1",
		"campus": "NB"
	}
	users_and_course_titles = {
		"<@624421039069200385>" : ["01:198:213", "01:198:336", "01:198:440", "01:198:428"]
	}
	users_and_indexes = {}
	
	all_courses = request(ALL_COURSES_URL, params)
	
	for user in users_and_course_titles:
		users_and_indexes[user] = get_indexes(all_courses, users_and_course_titles[user]);
	notify_discord("Sniper enabled")
	while True:
		all_open_sections = request(ALL_OPEN_SECTIONS_URL, params);		
		for user in users_and_indexes:
			for index in users_and_indexes[user]:
				if(index in all_open_sections):
					notify_discord("hello");


main();
