import praw
import time
import re
from pastebin import PastebinAPI

user_agent = "UBC Bot 0.1"
reddit = praw.Reddit(user_agent=user_agent)
reddit.login()
already_done = list()

while True:
	subreddit = reddit.get_subreddit("ubc")
	for submission in subreddit.get_hot(limit=10):
		if submission.id not in already_done:
			already_done.append(submission.id)
			#Parse title
			title = submission.title
			title_list = title.split(" ")
			for title_string in title_list:
				 course_number = None
				 course_name = None
				 #Course numbers will only ever be 3 numbers long
				 if title_string.len() == 3 and title_string.isdigit():
					course_number = title_string
				 #Check txt file if course_name is found in list of courses (CPSC, MATH, ENGL)
				 if check_course(title_string):
					course_name = title_string
			#Ensure that the title we checked contains both course_number and course_name
			if (course_number is not None) and (course_name is not None):
				 search_results = list(search(course_name + " " + course_number, subreddit="ubc", sort="new", period=None, limit=50))
				 for result in search_results:
				 # Construct post with list of posts with course_name + course_number
				 # and post in that submission.
	#sleep for an hour
	time.sleep(3600)

#Check string with .txt file
def check_course(course):
	with open("courses.txt") as course_file:
		for line in course_file:
			if re.search("\b{0}\b".format(course),line):
				return true
		return false
