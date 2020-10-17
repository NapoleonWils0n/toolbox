#!/usr/bin/env python3.7

try:
    import sys, re
    import urllib.request, urllib.parse, urllib.error, urllib.request
    from urllib.parse import urlparse
except:
    print("import error")

# main
def main(argv):
    
    # base url passed as first arg to script
    url=(argv[0])

    # download web page 
    def pagehtml(url):
        try:
           req = urllib.request.Request(url)
           req.add_header('User-Agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
           r = urllib.request.urlopen(req)
           the_page = r.read().decode('utf-8')
        except urllib.error.URLError as e:
            the_page = None
        return the_page

    # clappr page regex
    def clappr(thehtml):
        # find function, space, word and curly braces
        pageComp = re.compile('Clappr.Player\(\{[\s]+source:\s+[\'\"](.*?)[\'\"]')
        pageFind = pageComp.findall(thehtml)
        if pageFind:
            return pageFind
        else:
            print("no match")
            sys.exit()

    try:
        # download page
        page = pagehtml(url)
        # scraped html from page
        scrape = clappr(page)
        # get contents of scrape list
        m3u8 = scrape[0]
        print(m3u8)
    except (ValueError,IndexError):
        print("ValueError,IndexError")

if __name__ == "__main__":
    main(sys.argv[1:])
