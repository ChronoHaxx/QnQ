from difflib import SequenceMatcher
import numpy as np
from pathlib import Path

def levenshtein_ratio_and_distance(s, t, ratio_calc = False): #levenshtein ratio to check similarity of sentences
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

def mostSimilarSentencesStringFind(string1, string2, path_in_str) :   
    if string1 in string2 : # simple subset check for accurate copy paste question queries
        print(string1)
    else: 
        # algorithm to find ratio of similarity of substrings in a string (based on existence of words?) , refer : https://stackoverflow.com/questions/48117508/how-to-find-a-similar-substring-inside-a-large-string-with-a-similarity-score-in?noredirect=1&lq=1
        string1 = string1.split(' ')
        string2 = string2.split(' ')
        string1Length = len(string1)
        #print(string1Length)
        indices = [i for i, x in enumerate(string2) if x == string1[0] ] # get all occurences of string1[0], long repeates or is a lazy fix.. idk what happen
        #print(indices)
        similarityScoresLists = [None] * len(indices)
        for i in range(len(indices)):
            similarityScoresLists[i] = [None] * 2
        i = 0
        for x in indices :
            string2Joined = ' '.join(string2[x:x+string1Length-1]) # join the string1Length number of words after 1st index.
            #print(string2Joined)
            ratio = levenshtein_ratio_and_distance(' '.join(string1),string2Joined,ratio_calc = True)
            similarityScoresLists[i][0] = x
            similarityScoresLists[i][1] = ratio
            i += 1
        #print(similarityScoresLists)
        try :
            mostSimilarSentencesList = max(similarityScoresLists, key=lambda x: x[1])
        except:
            return 0
        #print(mostSimilarSentencesList) 
        mostSimilarSentencesIndex = mostSimilarSentencesList[0]
        mostSimilarSentencesRatio = mostSimilarSentencesList[1]
        print('Found at index of :' + str(mostSimilarSentencesIndex) + ' with ratio of ' + str(mostSimilarSentencesRatio) + ' from pdf file :' + path_in_str)
        mostSimilarSentencesString = ' '.join(string2[int(mostSimilarSentencesIndex):mostSimilarSentencesIndex + string1Length - 1])
        print(mostSimilarSentencesString)
        print("Similarity ratio :" + mostSimilarSentencesRatio)
        print("\n")
        return(mostSimilarSentencesRatio)

string1 = """Sir James Jeans, who was a great populariser of science, once described an atom of carbon
as being like six bees buzzing around a space the size of a football stadium.
"""
# iterate through all txt files in chemistrytxt folder
pathlist = Path('textfiles\\chemistry').glob('**/*.txt') 
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    # print(path_in_str)
    with open(path_in_str, 'r', encoding="utf8") as file:
        data = file.read()
        string2 = str(data).replace('\n', '') # remove newline so 
    try :
        if mostSimilarSentencesStringFind(string1,string2,path_in_str) > 0.9 :
            print('FOUND!')
            break
        else:
            continue
    except :
        continue
