class Node:
    # ALL NODES; Use id to select a node
    NODE_POOL = {}

    UrlToID = {}

    # Debugging, logging all import events
    SILENT = False

    def __init__(self, url, parentNodeId=None, statusCode=None) -> None:
        self.url = url

        origonalNode = self._doesAllReadyNodeExist()

        if origonalNode[0]:
            # if a node already exists with the same url
            print(f"Node with URL {self.url} already exists") if not Node.SILENT else None
            print(f"updating node with ID {origonalNode[1]}"+"\n") if not Node.SILENT else None
            self._isTwinNode = True
            # id of node with the same url
            self._twinsId = origonalNode[1]
            # figure out what to do with two nodes with the same id
        else:
            # if this node is origonal
            self._isTwinNode = False

            # adding parent node attribute
            self.parentNodesIds = set(parentNodeId) if parentNodeId else set()

            # Generating id
            self.id = self._generateId()
            print(f"{self.url} ID is {self.id}"+"\n") if not Node.SILENT else None 
            Node.NODE_POOL[self.id] = self    
            
            # ensuring no other node with same url exists
            Node.UrlToID[self.url] = self.id

            # updates parent nodes childrenNodes list
            if parentNodeId:
                self._updateParentNodeChildren(self.id)

            # what is the status code
            self.statusCode = statusCode

            self.childrenNodes = set()

        
        
    def addChildren(self, children):
        """Adds children to current node (and if this is a twin node add children to origonal node)

        Args:
            children (set(dict("url":Url, "statusCode":Status code))): The children to add
        """
        
        # when adding children, only add parent nodes to Node(parentNodeId) as 
        # this will update the current node with all the correct children nodes
        
        childrenNodes = []

        if self._isTwinNode:
            # This is a twin node
            id = self.twinsId

        else:
            # This is a origonal node
            id = self.id    

        for childInfo in children:
            childNode = Node(url=childInfo["url"], statusCode=childInfo["statusCode"])


            if childNode._isTwinNode:
                # if this node has already been created with the same url
                pass


            else:
                pass

         ##loop over all children in CHILDREN [from argument of current function]
                ## create Node instance 
                ## If node is not a twin
                    # add it to Nodes list
                ## If node is a twin
                    # update this nodes twins parent attribute
                    # do not add it to returning node list
                    # print out that there was a double up if SILENT = FALSE
    
        # return Nodes list

        
                

    def _generateId(self):
        # If current node has a parent [not none]
        if self.parentNodesIds:
            # determining position relative to other siblings
            parentNode = Node.NODE_POOL[list(self.parentNodesIds)[-1]]
            noSiblings = len(parentNode.childrenNodes)
            rawNickName = noSiblings + 1 # NickName; How the parent Node refers to current Node
                                         # Raw Nickname; what number child we are, not converted to base 26
        # If this is the first node in the genealogy
        else:
            # determining position relative to other siblings
            noSiblings = len(Node.NODE_POOL)
            rawNickName = noSiblings + 1 

        # goes from a number in base 10 to a number in base 26 [only using letters]
        nickName = self.__rawNickNameToNickName(rawNickName)
        
        # adding the parents id to the front of current id
        return f"{parentNode.id}:{nickName}" if self.parentNodesIds else nickName
    
    def __rawNickNameToNickName(self, rawNickName):
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nickName = ""
        
        if rawNickName == 0:
            return "0" 
        
        while rawNickName > 0:
            digit = rawNickName % 26
            nickName = digits[digit] + nickName
            rawNickName = rawNickName // 26
        
        return nickName

    def _updateParentNodeChildren(self, id):
        # updates the parents nodes children node list
        Node.NODE_POOL[list(self.parentNodesIds)[-1]].childrenNodes.add(id)

    def _updateTwinNodesParents(self, parentsId):
        Node.NODE_POOL[parentsId].parentNodesIds.add(self._twinsId)

    def _doesAllReadyNodeExist(self):
        """return True if a node with the same url exists and also the other nodes Id [bool, Id]
            If no node exist return False, and no Id [bool, Id]
        """

        if self.url in Node.UrlToID:
            # Node already exists
            idOtherNode = Node.UrlToID[self.url]
            return [True, idOtherNode]

        else:
            # This is a new node
            return [False, ""]

    

parent = Node("google.com")

child = Node("google.com/photos", parentNodeId=parent.id)

child2 = Node("google.com/photos")

print(child.parentNodesIds)
