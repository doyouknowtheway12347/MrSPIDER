import regex

def okURL(url):
    if regex.match(r"^\/[^\/]", url):
        print("relative url")
    elif regex.match(r"(?!\/)#", url) or regex.match(r"^#", url):
        print("anchor url")
    elif regex.match(r"^\/\/", url):
        print("Protocol-relative URLs")
    elif regex.match(r"%[0-9A-Fa-f]{2}+", url):
        print("Encoded")
    else:
        print("happy")

urls = ["/path/to/page.html",
        "https://example.com/page#section?param=value",
        "#anchor-on-current-page",
        "//example.com/path/to/pag",
        "https://example.com/path%20with%20spaces/file.php"]


for url in urls:
    print(url)
    okURL(url)
    print()




# _ work with relative URLS
            # /path/to/page.html
        # _ Fragment-only URLs
            # #anchor-on-current-page
            # https://example.com/page#section?param=value
        # _ Protocol-relative URLs
            # //example.com/path/to/page
        # _ Re directions 
            # ?
        # _ URLs with encoded characters
            #  https://example.com/path%20with%20spaces/file.php
 
        