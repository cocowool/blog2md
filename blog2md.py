import os, sys, glob, path, getopt
import html2text

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"hu:",["url"])
    except getopt.GetoptError:
        print("python blog2md.py -u <url>")
    for opt,arg in opts:
        if opt == "-h":
            print("python blog2md.py -u <url>")
            sys.exit(2)
        elif opt in ("-u", "-url"):
            print()
            checkSite(arg)
        else:
            print("python blog2md.py -u <url>")

if __name__ == "__main__":
    main(sys.argv[1:])