# -----------------------------------------------------
#    Name: Fahrin Bushra
#    ID: 1669159
#    CCID: bushra1
#    CMPUT 274, Fall 2021
#
#    Assignment 1
# -----------------------------------------------------

# Copyright 2020-2021 Paul Lu
import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer']


def printDictionary(dicto):
    ''' Prints a dictionary as a table of keys and values
    Code provided by @spencer from discord

    Arguments:
        dicto: A dictionary

    Returns:
        None
    '''
    print("{:<20}{}".format("Keys", "Values"))
    print("{:<20}{}".format("=" * 4, "=" * 6))
    for k in dicto:
        print("{:<20}{}".format(k, dicto[k]))
    return


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


# List of stopwords that will be ommited from input words during preprocessing
Stop_words = ["i", "me", "my", "myself", "we", "our",
              "ours", "ourselves", "you", "your",
              "yours", "yourself", "yourselves", "he",
              "him", "his", "himself", "she", "her",
              "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs",
              "themselves", "what", "which", "who", "whom",
              "this", "that", "these", "those",
              "am", "is", "are", "was", "were", "be",
              "been", "being", "have", "has", "had",
              "having", "do", "does", "did", "doing", "a",
              "an", "the", "and", "but", "if",
              "or", "because", "as", "until", "while", "of",
              "at", "by", "for", "with", "about", "against",
              "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down",
              "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when",
              "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no",
              "nor", "not", "only", "own", "same", "so", "than", "too",
              "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def both_present(word: str):
    '''Returns true if an integer and and a character are present in word

    Arguments:
        word (str)

    Returns:
        True if both integer and characters are present in word
        False otherwise
    '''
    digits = "0123456789"
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = "~!@#$%^&*()_-+=`<>?/.,\|}{[]''"":;"

    # Stores whether digits are present in word
    integers = False

    # Stores whether alphabets present in word
    alpha = False

    # Iterates over each digit in word checking
    # if digits/&characters present at the same time
    for char in word:
        if char in digits:
            integers = True
        if (char in alphabets) or (char in symbols):
            alpha = True
    return (integers and alpha)


def rem_digits(word: str):
    ''' Removes all integers from a word if both_present returns true

    Arguments:
        word (str)

    Returns:
        word (str): The word after removing the integers from it
    '''

    digits = "0123456789"

    # If both_present, iterates over each character in word
    # Removes the digits from it
    # Stores remaining alphabets/symbols in new_word and returns it
    if both_present(word):
        new_word = ''
        for char in word:
            if char not in digits:
                new_word = new_word + char
        return new_word
    else:
        return word


def rem_symbols(word: str):
    ''' Removes all symbols from word

    Arguments:
        word (str): input word to be processed

    Returns:
        new_word (str): word after removing the symbols from it
    '''

    symbols = "~!@#$%^&*()_-+=`<>?/.,\|}{[]''"":;"

    new_word = ''

    # Iterates over each charater of word
    # Stores all non symbol characters in word to new_word
    for char in word:
        if char not in symbols:
            new_word = new_word + char
    return new_word


def rem_stop_words(word_list: list):
    ''' Computes a new list which contains all words from word list
    that are not in stop_words_list

    Arguments:
        word_list (List[str]): Input list of strings

    Returns:
        new_list (List[str]):
            List that contains all the word in word_list
            that are not in word_list
    '''
    new_list = []

    # Iterates over each word in word_list
    # Sees if its present in stop_words_list
    for item in word_list:
        # If word not in stop_words_list, adds the word to new_list
        # Returns new_list
        if item not in Stop_words:
            new_list.append(item)
    return new_list


def turn_to_lower(word_list: list):
    ''' Modifies all words in word_list to lowercase

    Arguments:
        word_list (List[str]): List of words to be modified to lowercase

    Returns:
        None
    '''

    # Iterates over each word in word_list
    # Modifies the word completely to lower_case
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    return


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        super().__init__()  # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self, printSorted=True):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self, printSorted=True):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class ClassifyByTopN(ClassifyByTarget):
    # Subclass of ClassifybyTarget
    def __init__(self, lw=[]):
        super().__init__()  # Call superclass
        # self.type = str(self.__class__)
        return

    def target_top_n(self, tset, num=5, label=''):
        ''' Collects all words from all TrainingInstances of tset.
        Categorizes the words based on frequency
        The top num frequent words are included in output list.
        If there is a tie at the numth place, all tied words also added

        Arguments:
            tset (TrainingSet): Contains TrainingInstances
            num (int): The number of most frequent words to be taken
            label (str): Label of training instances to be processed

        Returns:
            None
        '''

        # Temporary dictionary to store count of all words
        # I.e. Words from all training instances processed
        temp_dict = {}

        # Gets all TrainingInstances from tset
        training_instances = tset.get_instances()

        # Iterates over all TrainingInstances
        for instance in training_instances:
            # If label of TrainingInstance matches input label
            # Then words in that Training instance is added to temp_dict
            if instance.inst["label"] == label:
                for word in instance.inst["words"]:
                    if word in temp_dict:
                        temp_dict[word] += 1
                    else:
                        temp_dict[word] = 1

        # Contains the values of temp_dict (frequencies of words) as a list
        # List is sorted in descending order
        # Duplicate items are removed from the list
        sorted_count = sorted(set(temp_dict.values()), reverse=True)

        # Is the sorted words list
        # Will contain the top num words sorted according to frequency
        sw_list = []

        # i is the while loop iterator
        # While loop will iterate (num - 1) times
        # Will store (num - 1) most frequent words from temp dict into sw_list
        i = 0

        # j stores the index of sorted count
        j = -1
        while i < num - 1:
            j = j + 1
            for item in temp_dict:
                if temp_dict[item] == sorted_count[j] and i < num - 1:
                    sw_list.append(item)
                    i = i + 1

        # Iterates over word in temp_dict
        # Stores the word with num-th frequency in the sw_list
        # Checks if the numth freq was in the current jth index of sorted_count
        for word in temp_dict:
            if temp_dict[word] == sorted_count[j] and (word not in sw_list):
                sw_list.append(word)

        # If the numth frequency was not at the jth frequrncy of sorted count
        # Then all words with (j+1)th freqeuncy added as numth word in sw_list
        if (len(sw_list) < num):
            for word in temp_dict:
                if temp_dict[word] == sorted_count[j + 1]:
                    if (word not in sw_list):
                        sw_list.append(word)

        # sw_list assigned as the new target_words_list
        self.set_target_words(sw_list)
        return


class TrainingInstance(C274):
    def __init__(self):
        super().__init__()  # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def preprocess_words(self, mode=''):
        ''' Preprocesses the words in a training instance in the following ways
            For each word:
            1. Converts to lowercase.
            2. Removes all punctuation and symbols.
            3. Removes all numbers UNLESS the token consists only of numbers.
            4. If the word is a stopword (see the list below), removes it.
            5. Adds it to a list of processed words.

        Arguments:
            mode (str)(optional argument):
                keep-digits: Does all the preprocessing except step 3
                keep-symbols: Does all the preprocessing except step 2
                keep-stops: Does all the preprocessing except step 4

        Returns:
            None
            Just modifies the training instance as specified above
       '''

        # Converts all words in bag of words to lowercase
        turn_to_lower(self.inst["words"])

        # Mode is a empty string, so does all the preprocessing
        if (mode == ''):
            # Removes symbols from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_symbols(self.inst["words"][i])

            # Removes digits from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_digits(self.inst["words"][i])

            # Removes stopwords from bag of words
            self.inst["words"] = rem_stop_words(self.inst["words"])

        # Does all the preprocessing but skips step 3
        elif (mode == "keep-digits"):
            # Removes symbols from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_symbols(self.inst["words"][i])

            # Removes stopwords from bag of words
            self.inst["words"] = rem_stop_words(self.inst["words"])

        # Does all the preprocessing but skips step 2
        elif(mode == "keep-symbols"):
            # Removes digits from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_digits(self.inst["words"][i])

            # Removes stopwords from bag of words
            self.inst["words"] = rem_stop_words(self.inst["words"])

        # Does all the preprocessing but skips step 4
        elif(mode == "keep-stops"):
            # Removes symbols from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_symbols(self.inst["words"][i])

            # Removes digits from words in bag of words
            for i in range(len(self.inst["words"])):
                self.inst["words"][i] = rem_digits(self.inst["words"][i])

        # If incorrect usage of mode
        else:
            print("Incorrect mode. Usage: python3 freq.py <mode>.\
            mode = keep-symbols/keep-stops/keep-digits")
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)


class TrainingSet(C274):
    def __init__(self):
        super().__init__()  # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def copy(self):
        '''Returns a deep copy of the TrainingSet
        '''
        return copy.deepcopy(self)

    def add_training_set(self, tset):
        ''' Adds all TrainingIstances in tset to the self TrainingSet

        Arguments:
            tset (TrainingSet):
                Instances from this training set will be added to self

        Returns:
            None
        '''
        # Iterates over all TrainingInstances in tset
        # Adds a deeep_copy of all the instances to self TrainingSet
        for instance in tset.get_instances():
            self.inObjHash.append(copy.deepcopy(instance))

        # Iterates over all unparsed lines in tset
        # Adds a deep_copy of te lines to self TrainingSet
        for line in tset.get_lines():
            self.inObjList.append(copy.deepcopy(line))
        return

    def return_nfolds(self, num=3):
        ''' Splits the current TrainingSet into num tsets

        >>> (A, B, C, D, E, F, G).return_nfolds(3)
        [ (A, D, G), (B, E), (C, F) ]
        Here each tuple is a training set
        Each element of a tuple are the TrainingInstances inside the sets

        Arguments:
            num  (int) (optional): The number of partitions to be made
        Returns:
            List of the num training sets
        '''

        # Stores the length of the current training set
        number = len(self.inObjHash)

        # All the partioned training sets will be stored in LIST
        LIST = []
        instances = self.get_instances()
        lines = self.get_lines()

        # If the current tset can be divided evenly into num partitions
        if number % num == 0:
            # Length of largest partition
            partition_len = number//num

            # Iterates num times to store num partitions in LIST
            for i in range(num):

                # k is the emporary training set
                # Will hold the instances of each partition
                k = TrainingSet()

                # Applies the robin hood method of partitioning
                # Will store every [i + j*num]th instance of tset to k

                for j in range(partition_len):
                    k.inObjHash.append(copy.deepcopy(instances[i + j*num]))
                    k.inObjList.append(copy.deepcopy(lines[i + j*num]))
                LIST.append(copy.deepcopy(k))
            return LIST
        else:
            rem = number % num
            partition_len = (number+(num - rem)//num)
            for i in range(num):

                # k is the emporary training set
                # Will hold the instances of each partition
                k = TrainingSet()

                # Applies the robin hood method of partitioning
                # Will store every [i + j*num]th instance of tset to k
                for j in range(partition_len):
                    if (i + j*num) < number:
                        k.inObjHash.append(copy.deepcopy(instances[i + j*num]))
                        k.inObjList.append(copy.deepcopy(lines[i + j*num]))
                    else:
                        break
                LIST.append(copy.deepcopy(k))
            return LIST

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=''):
        ''' Calls preprocess_words on each TrainingInstance in TrainingSet

        Arguments:
           mode (str)(optional argument):
               keep-digits: Does all the preprocessing except step 3
               keep-symbols: Does all the preprocessing except step 2
               keep-stops: Does all the preprocessing except step 4

        Returns:
           None
           Modifies all the training instance in TrainingSet as specified
        '''
        training_instances = self.get_instances()
        for instance in training_instances:
            instance.preprocess_words('')
        return


# Very basic test of functionality
def basemain():
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()
