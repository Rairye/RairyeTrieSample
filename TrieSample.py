class Node():
    
    def __init__(self, name):
        self.__name__ = name
        self.__children__ = {}
        self.__word_end__ = False
        
    def __add_child__(self, child):
            self.__children__[child] = Node(child)

    def __has_child__(self, child):
            return child in self.__children__
        
    def __has_children__(self):
            return self.__children__ != {}
        
    def __get_children__(self):
        return self.__children__

    def __get_name__(self):
        return self.__name__
  
class Trie():
    
    def __init__(self):
        self.__trie_dict__ = {}
        self.__results__ = set([])
        
    def add(self, word):
        word_len = len(word)
        if not word[0] in self.__trie_dict__:
            self.__trie_dict__[word[0]] = Node(word[0])
        current_node = self.__trie_dict__[word[0]]
        i = 1
        while i < word_len - 1:           
            if not current_node.__has_child__(word[i]):
                current_node.__add_child__(word[i])
            current_node = current_node.__children__[word[i]]
            i+=1
        if not current_node.__has_child__(word[i]):
                current_node.__add_child__(word[i])       
        current_node = current_node.__children__[word[i]]
        current_node.__word_end__ = True

    def find(self, word):
        word_len = len(word)
        if not word[0] in self.__trie_dict__:
            return False        
        i = 1
        current_node = self.__trie_dict__[word[0]]
        while i < word_len -1:
            if not current_node.__has_child__(word[i]):
                return False
            current_node = current_node.__children__[word[i]]
            i+=1    
        try:
            current_node = current_node.__children__[word[i]]
        except:
            return False
        if current_node.__word_end__:
            return True
        return False
           
    def starts_with(self, word):
        #Recursive method for finding the ends of words.
        def __find_end__(node, word):
            if not node.__has_children__():
                self.__results__.add(word)   
                return
            else:
                if node.__word_end__:       
                    self.__results__.add(word)
                children = node.__get_children__()    
                for child in children:
                    temp = children[child]    
                    name = word + temp.__get_name__()            
                    __find_end__(temp, name)

        self.__results__ = set([])
        word_len = len(word)
        if word_len == 0:
            print("Error: String too short.\n")
            return
        else:
             match = True
             i = 1
             try:
                 current_node = self.__trie_dict__[word[0]]
             except:
                 match = False
             while i < word_len and match:
                if not current_node.__has_child__(word[i]):
                    match = False
                    break
                current_node = current_node.__children__[word[i]]
                i+=1        
             if not match:
                print("Error: Found no strings which start with \"{}\".\n".format(word))
                return
             else:   
                if current_node.__word_end__:
                    self.__results__.add(word)
                children = current_node.__get_children__()
                for child in children:
                    temp = children[child]
                    name = word + temp.__get_name__()                
                    __find_end__(temp, name)    
                print("Results:", end = " ")
                for result in self.__results__:
                    print(result, end = " " )
                print("\n")
                
#Demonstration of Trie implementation
if __name__ == "__main__":
  
    T = Trie()
    
    #Words to be added to the Trie.
    words = ["app", "apple", "application", "appetite", "answer", "analog", "abormal", "abnormality", "advice", "addition", "additive", "approval", "appointment", "analogy", "ab",
             "abdonimal", "abdominals", "ask", "asking", "ban", "banana", "band", "bandit", "bandana", "boy", "boil", "buoyant", "add-on"]

    for w in words:
        T.add(w)

    print("Find \"a\": {}\n".format(T.find("a")))
    
    print("Find \"app\": {}\n".format(T.find("app")))
    
    print("Find \"appl\": {}\n".format(T.find("appl")))
    
    print("Find \"application\": {}\n".format(T.find("application")))

    print("Find \"applffes\": {}\n".format(T.find("applffes")))

    print("Find \"applffes\": {}\n".format(T.find("apples")))

    print("Starts with \"ap\"")  
    T.starts_with("ap")
    
    print("Starts with \"ab\"")  
    T.starts_with("ab")
    
    print("Starts with \"ad\"")  
    T.starts_with("ad")
    
    print("Starts with \"addi\"")  
    T.starts_with("addi")
    
    print("Starts with \"\"")  
    T.starts_with("")

    print("Starts with \"b\"")  
    T.starts_with("b")
    
    print("Starts with \"ban\"")  
    T.starts_with("ban")
    
    print("Starts with \"bo\"")  
    T.starts_with("bo")
    
    print("Starts with \"bananas\"")  
    T.starts_with("bananas")
    
    print("Starts with \"c\"")  
    T.starts_with("c")

    print("Starts with \"asfsadfasdrwe\"")  
    T.starts_with("asfsadfasdrwe")
