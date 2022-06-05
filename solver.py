#   Arthure Antony
#   J Qnax Ljw Kn Jwhxwn,
#   Nenw J Vjw Mxrwp Bxvncqrwp
#   Jb Brvyun Jwm Anjbbdarwp Jb
#   Ydccrwp J Lxjc Jaxdwm J Hxdwp
#    Kxh'b Bqxdumnab Cx Unc
#    Qrv Twxf Cqn
#   Fxaum Qjmw'c Nwmnm.

import argparse,chardet,sys

def solver(chars,n):
    l = len(chars)
    for i in range(l):
        if(chars[i].isalpha()):
            ar = ord(chars[i])
            t = ar-n
            if(chars[i].isupper()):
                if(t<65):
                    t = 91 -(65-t)
                print(chr(t),end="")
            else:
                if(t<97):
                    t = 123 - (97-t)
                print(chr(t),end="")
        else:
            print(chars[i],end="")

def process(txt):
    if(args.rot == 'b'):
        print("BACKWARD ROTATION")
        if(args.number):
            print("\n\nROT - " + str(args.number) + "\n")
            solver(txt,args.number)
        else:
            for num in range(1,27):
                print("\n\nROT - " + str(num) + "\n")
                solver(txt,num)
    else:
        print("FORWARD ROTATION")
        if(args.number):
            print("\n\nROT - " + str(args.number) + "\n")
            solver(txt,27 - args.number-1)
        else:
            for num in reversed(range(1,27)):
                print("\n\nROT - " + str(27 - num) + "\n")
                solver(txt,num-1)



encodings = ['utf-8', 'windows-1250', 'windows-1252','utf-16']
parser = argparse.ArgumentParser(description ='Rotate Letters')
parser.add_argument('-i', '--input', dest ='filename',help ='input file')
parser.add_argument('-t','--text', dest ='text', help ='Plain Text')
parser.add_argument('-o','--output', dest ='outputfilename',help ='output file name')
parser.add_argument('-n','--number', dest ='number', type=int,help ='Rotation Number')
parser.add_argument('-r','--rotation', dest ='rot', choices = {'f', 'b'},default ='b', help ='rotation direction f = forward b = backward')
args = parser.parse_args()

if(args.filename):
    try:
        f = open(args.filename,'rb')
        txt = f.read()
        f.close()
        txt = txt.decode(chardet.detect(txt)['encoding'])
        if(args.outputfilename):
            stdout = sys.stdout
            sys.stdout = open(args.outputfilename, 'w')
            process(txt)
            sys.stdout.close()
            sys.stdout = stdout
        else:
            process(txt)
    except:
        print("An Error Occured while Opening the File..")
        exit()
elif(args.text):
    if(args.outputfilename):
            stdout = sys.stdout
            sys.stdout = open(args.outputfilename, 'w')
            process(args.text)
            sys.stdout.close()
            sys.stdout = stdout
    else:
        process(args.text)
else:
    print("No input provided")
    exit()
