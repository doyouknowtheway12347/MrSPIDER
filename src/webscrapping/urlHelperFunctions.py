import urllib.parse
import regex

class Url:
    _maxRecursionDepth = 1
    _SILENT = False

    def __init__(self, unPassedUrl, parentUrl) -> None:
        self.unPassedUrl = unPassedUrl
        self.parentUrl = parentUrl

        self._checkUrl()
    
    def _checkUrl(self, _recursionDepth=0):
        if _recursionDepth > Url._maxRecursionDepth:
            self.url = ""  
            print(f"Unknown error encountered with URL: {self.unPassedUrl}") if not Url._SILENT else None
            return
        
        if regex.search(r"^\/[^\/].*$", url): 
            print("relative url")

        elif regex.search(r"^.*[^\/=]#.*$|^#.*$", url): 
            print("anchor url")

        elif regex.search(r"^\/\/.*$", url): 
            print("Protocol-relative URLs")

        elif regex.search(r"^.*(%[0-9A-Fa-f]{2}.*)+$", url):
            print("Encoded")
        else:
            print("Good URL")
            self.url = self.unPassedUrl
            print(f"URL: {self.url} is acceptable") if not Url._SILENT else None
            return
        
        self._checkUrl(_recursionDepth=_recursionDepth+1)

        

    
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
 
  