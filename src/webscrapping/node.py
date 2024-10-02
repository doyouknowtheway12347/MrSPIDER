class Node:
    # ALL NODES; Use id to select a node
    _ALL_NODE_INSTANCES = {}

    _UrlToID = {}

    # Debugging, logging all import events
    _SILENT = False

    def __init__(self, url, parentNodeId=None, statusCode=None) -> None:
        self.url = url

        origonalNode = self._doesAllReadyNodeExist()

        if origonalNode[0]:
            # if a node already exists with the same url
            print(f"Node with URL {self.url} already exists") if not Node._SILENT else None
            print(f"Using current instance as a pointer towards node with ID: {origonalNode[1]}"+"\n") if not Node._SILENT else None
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
            print(f"ID: {self.id} has URL {self.url} "+"\n") if not Node._SILENT else None 
            Node._ALL_NODE_INSTANCES[self.id] = self    
            
            # ensuring no other node with same url exists
            Node._UrlToID[self.url] = self.id

            # updates parent nodes childrenNodes list
            if parentNodeId:
                self._updateParentNodeChildren(self.id)

            # what is the status code
            self.statusCode = statusCode

            self.childrenNodesIds = set()
   
    def addChildren(self, children):
        """Adds children to current node (and if this is a twin node add children to origonal node)

        Args:
            children (set(tuple(Url, Status code), ...)): The children to add
        """
        
        # list of all origonal children nodes
        childrenNodes = []

        # looping over all children 
        # eg of children
            # children = {("youtube.com", 200), ("music.youtube.com", 200)} 
        for childInfo in children:
            # creates Nodes class instance with attributes stated from childInfo variable
            childNode = Node(url=childInfo[0], statusCode=childInfo[1], parentNodeId=self.id)


            if childNode._isTwinNode:
                # if this node has already been created with the same url
                # ie creating a new link with the other twin node
                
                # updates the parentNodesIds attribute of the twin to the current Node instance
                childNode._updateTwinNodesParents(self.id)
                print(f"Updating ID: {childNode._twinsId} with URL {Node._ALL_NODE_INSTANCES[childNode._twinsId].url} parents with ID: {self.id}" + "\n") if not Node._SILENT else None

                # updating childrenNodesIds of current instance with twin node 
                self.childrenNodesIds.add(childNode._twinsId)
            else:
                # appending origonal node to returning list
                childrenNodes.append(childNode)

                # updating childrenNodesIds of current instance with twin node
                self.childrenNodesIds.add(childNode.id)

        return childrenNodes
                
    def _generateId(self):
        # If current node has a parent [not none]
        if self.parentNodesIds:
            # determining position relative to other siblings
            parentNode = Node._ALL_NODE_INSTANCES[list(self.parentNodesIds)[-1]]
            noSiblings = len(parentNode.childrenNodesIds)
            rawNickName = noSiblings + 1 # NickName; How the parent Node refers to current Node
                                         # Raw Nickname; what number child we are, not converted to base 26
        # If this is the first node in the genealogy
        else:
            # determining position relative to other siblings
            noSiblings = len(Node._ALL_NODE_INSTANCES)
            rawNickName = noSiblings + 1 

        # goes from a number in base 10 to a number in base 26 [only using letters]
        nickName = self.__rawNickNameToNickName(rawNickName)
        
        # adding the parents id to the front of current id
        return f"{parentNode.id}:{nickName}" if self.parentNodesIds else nickName
    
    def __rawNickNameToNickName(self, rawNickName):
        # black magic!!!!!!!!!!!!!!!!!!!
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
        Node._ALL_NODE_INSTANCES[list(self.parentNodesIds)[-1]].childrenNodesIds.add(id)

    def _updateTwinNodesParents(self, parentsId):
        # updates the parentNodesIds attribute of the twin node
        Node._ALL_NODE_INSTANCES[self._twinsId].parentNodesIds.add(parentsId)

    def _doesAllReadyNodeExist(self):
        """return True if a node with the same url exists and also the other nodes Id [bool, Id]
            If no node exist return False, and no Id [bool, Id]
        """

        if self.url in Node._UrlToID:
            # Node already exists
            idOtherNode = Node._UrlToID[self.url]
            return [True, idOtherNode]

        else:
            # This is a new node
            return [False, ""]


# eg
# parent = Node("google.com")
# otherNode = Node("google.com/photos")
# googleChildren = parent.addChildren({("google.com/photos", 200),})
# print(otherNode.parentNodesIds)



