import read as r
import listen as l
import hello_time
import time

name = 'Tam'
sayf = ['say','bye']

def main():
    while True:
        say = input()
        if 'hello' in say:
            r.talk(hello_time.hello(name))
        elif 'bye' in say:
            r.talk('Good bye')
            break
        elif 'now' in say:
            r.talk(hello_time.get_time(say))


        else:
            r.talk(sayf[1])



main()