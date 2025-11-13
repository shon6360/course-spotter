import requests, time

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1438576405490307122/SFSjV9tXIZMqL5dVKceg7hJYGfzhRgplky_DJW8wyHKzuGw7j2gLSJo_HocPp7y5A4Ie"

def get_courses(subject, semester, campus, level):
	url = "https://sis.rutgers.edu/oldsoc/courses.json"
	params = {
		"subject": subject,
		"semester": semester,
		"campus": campus,
		"level": level
		}
	try:
		response = requests.get(url, params=params)
		response.raise_for_status()  # Raise an error for bad responses
		courses = response.json()
		return courses

	except requests.exceptions.RequestException as e:
		print(f"Error: {e}")

def print_courses(courses):
		for course in courses:
			print(f"Course: {course['title']}")
			for section in course['sections']:
				print(f"  Section: {section['number']} - Seats: {section['openStatus']}")


def notify_discord(msg):
	requests.post(DISCORD_WEBHOOK, json={"content": msg}, timeout=10)

#main
subject = "198"
campus = "NB"
level = "U"
semester = "12026"

courses = ["213", "336"]

while True:
	all_courses = get_courses(subject, semester, campus, level)
	for course in all_courses:
		if(course["courseNumber"] in courses):
			#notify_discord((course["title"] + " PRESENT!"))
			if (int(course["openSections"]) > 0): 
				for section in course["sections"]:
					if(section["openStatus"]):
						notify_discord(course["title"] + " IS OPEN, SECTION: " + section["number"] + " INDEX: " + section["index"]);
	time.sleep(1)


