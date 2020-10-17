#!/usr/bin/env python3.7

import sys, os, re, os.path, mimetypes
from urllib.parse import unquote

def main(argv):

    if len(argv) == 0: # no arguments passed to script
        print("No arguments passed to script")
        sys.exit()
    elif len(argv) > 1: # too many arguments passed to script
        print("Too many arguments passed to script")
        sys.exit()

    # open text file and use readlines to store in a list
    def readpage(page):
        if os.path.isfile(page):
            if mimetypes.guess_type(page)[0] == 'text/plain':
                with open(page, 'r') as file:
                    page = file.readlines()
                return page

    # text file to read in
    file_input=(argv[0])
    text=readpage(file_input)

    # m3u8 tags
    extm3u='#EXTM3U'
    extint='#EXTINF:0,'

    with open('playlist.m3u', 'w') as file:
        file.write("%s\n" % extm3u)
        for url in text:
            urlsplit=url.rsplit('/', 1)[-1] # split url on list /
            vfilename=extint+unquote(unquote(urlsplit)) # url decode and prefix with extint
            file.write("%s\n" % vfilename)
            file.write("%s\n" % url)

#if __name__ == "__main__":
#    main(sys.argv[1:])

def entry():
    main(sys.argv[1:])
