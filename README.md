The initial inspiration for this was seeing a lot of posts on r/ubc with people asking (hey is cpsc 221 hard? what about compared to 213?). CLEARLY not searching and they should drop out like the double digit iq flunkies they will be. this bot is to do this for them.

1. gets top 10 hot submissions on ubc every hour (if submission has already been looked at then it is discarded)
2. parses submission title to see if it contains a course title + course number
      yes there is future features that may be implemented here in the sense of looking only for a course title and being able to more         exactly determine what the submitter is looking for by taking key strings
3. checks for the course number by checking if the string is digits and if its 3 characters in length
4. checks for the course name by (get this part) checking if that string is found in a 250~ line text file (don't yell at me Q-Q)
5. does a reddit search with that course title + course number and then constructs a post of no more than 50 search results and posts it in that submission. (the initial implentation was to do an automatic anonymous pastebin post and to only post that linke but since then the pastebin devs have been ASSHOLES so it's out of the question).

clearly this bot is not done since there's still posting to be done but i got lazy and there was NO documentation on what the actual structure of a search result looked like and im already bored of this. its nitty and gritty but it was only 30 minutes of work and i just wanted to try making a reddit bot as ive seen so many already. 

all of this was working until i got the point where i was constructing the bot's post, and it's at that point i said you know what this is boring and fuck it. this code is up for anybody to take :)

props to praw for making the job seemless. 
