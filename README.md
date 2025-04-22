# zenith
> Outline a brief desription of your project.
> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [Description](#description)
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## Description
- Team: Julian Zarazua, Bryan Carreon, Jazmin Rodriguez, Bryan Montoya, Samantha Martinez

- What We Are Creating: We are creating a website that generates workout routines for people who workout.

- Who We Are Doing It For: We are doing this for beginners who are getting into fitness, people who want to work on
  a certain muscle/muscles, or for those who just enjoy working out and want a website that might help them get fit.

- Why We Are Doing This: We are creating this website because we want to help out someone out there who is new to fitness routines
- and because we want to make it easier for our users to find a routine that will benefit them.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## General Information
![Alt text](templates/Zenith_Logo.png)



## Technologies Used
- HTML
- CSS
- Java Script
- Figma
- Firebase
- Flask
- Open Ai


## Features

## Sprint 1

#### Contributions

**Samantha**:

- Create Workout Routine Page CP-12 Workout Routine Webframe: The user who is looking for a workout routine can generate a routine that best accomodates what they are looking for. I designed the workout routine page by using HTML and CSS. Now we have a functioning website that lets the user pick a muscle group that they want to workout on. https://bitbucket.org/cs3398-callisto-f24/zenith/commits/6a554f2ead0b45336be0e8dd52a48823b16cb5bc

- Integrate Workout Plan API CP-11 API Integration: This API can help users have a structured workout plan by having access to a database of exercises and workout plans. The api that I ended up using was Exercise Database. The way this api works is by generating workouts based on the musle group that the user chooses. https://bitbucket.org/cs3398-callisto-f24/zenith/pull-requests/7 

**Bryan Montoya**:

- Create Login, Logout and Sign up pages. Including database setup for each user session. Using HTML, CSS and Python I created each page so that each user can successfuly log in to our app and can sign out when needed. https://bitbucket.org/cs3398-callisto-f24/zenith/commits/branch/CP-59-connect-user-account-to-database
- Create the home page for user navigation throughout our app. Using HTML, CSS and Python I created the home page so that each user can navigate our app and switch from page to page when wanting to access all of our features. https://bitbucket.org/cs3398-callisto-f24/zenith/commits/branch/feature%2FCP-6-home-page-layout
- [https://cs3398-callisto-f24.atlassian.net/jira/software/projects/CP/boards/1?assignee=712020%3A54b38500-7ff6-442f-bea5-9ab3175c9b96]

**Julian Zarazua**:
- Create a Contact Form
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-48?atlOrigin=eyJpIjoiMzIwOGZmYzJiZDk0NDljYjkwNzlmMWI5MWQzZmZkMjQiLCJwIjoiaiJ9]
- Add a Confirmation Page
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-52?atlOrigin=eyJpIjoiZmI2OGMyMTAxYzI3NGYxNmIxZTFlNTA3ZDM0MzczOTkiLCJwIjoiaiJ9]
- Create base Flask app
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-54?atlOrigin=eyJpIjoiYjg4MTQwYTUxOGMyNDhhNzlkZDk0M2FjODUyZTEwODkiLCJwIjoiaiJ9]
- Display Business Hours and Support Availability
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-51?atlOrigin=eyJpIjoiZmRjMjMyM2UyMGQwNDNkOTg0NjJiMGE2ZWI3YmYyZmYiLCJwIjoiaiJ9]
- Display Contact Information
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-50?atlOrigin=eyJpIjoiZGUwMGE1ZDE2YTJjNGVhMWFhODk0OGU5MzMyYjFkOGUiLCJwIjoiaiJ9]
- Integrate Email Sending Functionality
- [https://cs3398-callisto-f24.atlassian.net/browse/CP-49?atlOrigin=eyJpIjoiZDRkOWMxZWMzYWMzNDhkZGJiYzc4NjlmYzhkNGFiNTQiLCJwIjoiaiJ9]
**Bryan Carreon**:
- Created a Base profile HTML page
-[https://bitbucket.org/cs3398-callisto-f24/zenith/branch/feature/CP-14-create-a-simple-profile-page]
- Added CSS styling to the profile page
- [https://bitbucket.org/cs3398-callisto-f24/zenith/branch/feature/CP-15-add-css-styling-to-the-profile-pag]
- Connected to profile page to the navigation menu
- [https://bitbucket.org/cs3398-callisto-f24/zenith/branch/feature/CP-55-connect-profile-to-home]

**Jazmin Rodriguez**
- Created a Calorie Calculator page
- [https://cs3398-callisto-f24.atlassian.net/jira/software/projects/CP/boards/1/backlog?epics=visible&issueParent=10037]
- created a Progress Tracker page
- [https://cs3398-callisto-f24.atlassian.net/jira/software/projects/CP/boards/1/backlog?epics=visible&issueParent=10036]



## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
The dependencies for this app are listed in `requirements.txt`. To install the dependencies, run this within a virtual environment:

```sh
pip install -r requirements.txt
```

Once the dependecies are installed, the server can be run using:

```sh
python runserver.py
```

## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: In Progress


## Next Steps

**Samantha**:

- Make the workouts given in the workout routines more descriptive. 
- Provide the workouts given with youtube links or pictures to guide the user.
- The workout routine page cuts off, so I need to make a bug fix so that it shows the whole page.

**Bryan M**
- Make user navigation smoother and update the home page.
- Make UI look prettier
- Integrate Spotify API to app
**Bryan C**
- Connect a database to hold user information and save it for their session
- possibly run on a server
- implement a friends feature to view eachother progress/goals
**Julian Z**
- Improve the Contact Page UI
- Improve the flow of the application
- Improve the architecture of code
**Jazmin R**
- Implement the calcolarie code so that it can calculate the calories properly.
- Connect the progress tracker to the workout routine page so the same workouts appear

## Features

## Sprint 2

#### Contributions

**Samantha**:

- Connect work out routine page to home page SCRUM-61 Homepage link to workout routine page
- Made a button in the homepage that leads directly to the workout routine page. 
- https://bitbucket.org/cs3398-callisto-f24/zenith/commits/branch/feature%2FCP-60-connect-workout-routine-page-to-ho

- Build a workout timer: SCRUM-92 Workout timer
- https://bitbucket.org/cs3398-callisto-f24/zenith/commits/branch/feature%2FSCRUM-91-build-a-workout-timer

**Jazmin**

- Connect an APi to the Calculator page 
https://cs3398-callisto-fall24.atlassian.net/jira/software/projects/SCRUM/boards/1?selectedIssue=SCRUM-81
- provided a done/undo option in the progress page
https://cs3398-callisto-fall24.atlassian.net/jira/software/projects/SCRUM/boards/1?selectedIssue=SCRUM-87


**Julian**:

- Create Meal Suggestion Page: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-98
- Set Up AI Meal Suggestion: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-94
- Implement Workout Form and HTML: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-104
- Display Recipe Suggestion: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-104
- Implement AI generated Workout: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-96
- Set Up Recipe Search API: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-100

**Bryan Montoya**:

- Restructured App and Made UI Better: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-53
- Created database on firebase and connected it to app: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-67
- Implemented User authentication requirements to be able to access home page and every other page in app, 
  also made it possible for app to know who was logged in, all through firebase authentication: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-69
- Added motivational quotes to home page with a quotes API: https://cs3398-callisto-fall24.atlassian.net/browse/SCRUM-71

## Next Steps

**Samantha**: 

- I want to implenet a save feature for workouts that a user likes
- I want to add a feature that lets a user track their sets and reps for their workouts
- I need to fix my timer because it does not want to load when the button is clicked on the homepage

**Jazmin**
- I want to link the saved workouts from the profile to the progress page
- Fix the code so that the output calories comes out clearly in the calculator page

**Bryan Montoya**:

- I will connect the users to database and make it possible for the user to see their data when they log in to their account.
- Will add forgot password option.
- Attempt to deploy app through bitbucket pipelines.
- Fix some UI issues. 
- Allow users to be able to see other peoples progress if they are friends.
- Will attemot to implement some sort of game within the app for user accomplishments.
- Attempt to link spotify into app to display users library and recommend songs based on what workouts the user is doing.


## Acknowledgements
Give credit here.
- Parts of this project were based on this tutorial [https://www.youtube.com/watch?v=dam0GPOAvVI.]
