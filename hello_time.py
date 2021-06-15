from time import strftime, time

def hello(name):
    day_time = int(strftime('%H'))
    say = ''
    if day_time < 12:
        say = "Good moning {}.".format(name)
    elif 12 <= day_time < 18:
        say = "good afternoon {}.".format(name)
    else:
        say = "good evening {}. ".format(name)
    return say

def get_time(text):
    say = ''
    if "time" in text:
        say ='Now: ' + strftime("%H and %M")
    elif "day" in text:
        say = 'Today ' + strftime("Month: %B, day: %d and year: %Y")
    else:
        say = "I don't know"
    return say
