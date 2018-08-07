# Insights

How many times have you gotten a nugget of wisdom from a teacher, book, or friend that you want to implement in your daily life? Maybe you want to spend more time with your family or pursue your passions or maybe just live more purposefully than you do now. But if you're like me then you will live by this advice for 2 or 3 days then completely forget it the next days! 

Insights is an Android Application, web app, and Amazon Alexa Skill to help users remember this advice that they were given. Insights hopes to help you live the life you want to live by writing down and reminding you of the advice that was given to you. Everyday one piece of advice from your list is delivered to your inbox or apart of your Morning Update on Alexa to remind you to live the life you want to live. 

Join us and lets live a more purposeful life.

## MVP

1. Backend server and database
	- stores users and email addresses
	- stores all insight for a user
	- stores list of insight given for previous days
	- keeps count of amount of insight

1. Website
	- allows login via facebook or google
	- settings page: set email address, whether or not you want email updates
	- viewing of all insights
	- add an insight
	- delete an insight

1. Android App
	- allows login via facebook or google
	- settings page: set email address, whether or not you want email updates
	- viewing of all insights
	- add an insight
	- delete an insight

1. Alexa Skill
	- allows login via facebook or google
	- get an insight as a daily update
	- get number of insights in the database
	- add an insight (via a 2-multi step prompt - first the user asks to add an insight and then is prompted to say the insight. Afterwards the user may add an author or note or source)

## Stack

Backend 
	- MongoDB (document store)
		- Schemas:
			- Person (name, join date, email, facebook/google login)
			- Insight (insight, source, notes, link, author, date)
	- Framework: Django/NodeJS/Flask
		- MEAN Stack with NodeJS - https://www.mongodb.com/blog/post/building-your-first-application-mongodb-creating-rest-api-using-mean-stack-part-1
		- Flask and using the Python connector to Mongo - https://medium.com/@peregringaret/a-different-stack-angular-flask-mongodb-780b44e10afd
Alexa Skill
	- Intents:
		- Add an Inisight
		- Number of Insights
		- Get Daily Insight
Android App
Website
	- FrontEnd Framework: ?


## Future features
	- suggested insights
	- curation of insights
	- adding goals and habits (along with advice) to remind you of your goals - rememeber why you have these goals
	- scheduling
	- share an insight with a friend or on social media
	- cool memes and text effects for advice to post to social media + to influencers
	- affirmations

## Contact

Please feel free to contact the lead developer and inventor at neeasthana@gmail.com