from time import strftime
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