import urllib.parse
import regex

class Url:
    def __init__(self, unPassedUrl, parentUrl) -> None:
        self.unPassedUrl = unPassedUrl
        self.parentUrl = parentUrl

        acceptableUrl = self._checkUrl()

        # if acceptableUrl["not useable"]:
        #     self.returningUrl = acceptableUrl["correction function"](self.unPassedUrl, self.parentUrl)
        # else:
        #     self.returningUrl = self.unPassedUrl
    
    def _checkUrl(self):
        if regex.match(r"^\/[^\/]", self.unPassedUrl):
            print("relative url")
        elif regex.mat

    
url = Url("/path/to/page.html", "www.google.com")
    
    
    # turns url to a useful form
        # _ check if url is useable
            # checks for
                # relative
                #  
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
 
  