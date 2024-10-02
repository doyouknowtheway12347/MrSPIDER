import urllib.parse
import regex

class Url:
    _maxRecursionDepth =1 
    def __init__(self, unPassedUrl, parentUrl) -> None:
        self.unPassedUrl = unPassedUrl
        self.parentUrl = parentUrl

        self._checkUrl()
    
    def _checkUrl(self, _recursionDepth=3):
        if regex.match(r"^\/[^\/]", self.unPassedUrl):
            print("relative url")
        elif regex.match(r"[^\/=\-\.\+\?_~]#|^#", self.unPassedUrl):
            print("anchor url ")
        elif regex.match(r"^\/\/", self.unPassedUrl):
            print("Protocol-relative URLs")
        elif regex.match(r"%[0-9A-Fa-f]{2}+", self.unPassedUrl):
            print("Encoded")
        else:
            print("happy")
        

    
url = Url("#path/to/page.html", "www.google.com")
    
    
    # turns url to a useful form
        # _ check if url is useable
            # checks for
                # relative
                # anchor url
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
 
  