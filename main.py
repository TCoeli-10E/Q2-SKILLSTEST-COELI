# uhhhhh skills test fr
from pyscript import display, document

basketball = {
    'name of club' : 'basketball varsity',
    'description' : 'basketball varsity team of the school',
    'meeting times' : 'every monday 3:00-5:00 pm',
    'location' : 'quadrangle',
    'club moderator' : 'sir bjorn amargo',
    'number of members' : 30 
}     #dictionary for basketball club
soc_sci = {
    'name of club' : 'social science club',
    'description' : 'a club for social science enthusiasts',
    'meeting times' : 'every tuesday 2:30-4:00 pm',
    'location' : 'room 703',
    'club moderator' : 'maam neena libramonte',
    'number of members' : 25 
}    #dictionary for social science club
band = {
    'name of club' : 'school band',
    'description' : 'the official school band',
    'meeting times' : 'every friday 2:30-4:00 pm',
    'location' : 'band room',
    'club moderator' : 'sir almine',
    'number of members' : 50
}    #dictionary for school band  

def display_club_info1(e):
    club_info = basketball
    bball_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("output").innerText = bball_output

def display_club_info2(e):
    club_info = soc_sci
    soc_sci_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("output").innerText = soc_sci_output

def display_club_info3(e):
    club_info = band
    band_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("output").innerText = band_output

def clear_club_info(e):
    document.getElementById("output").innerText = ""








