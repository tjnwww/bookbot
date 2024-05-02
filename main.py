def main():
  
    path = "books/frankenstein.txt"
    getReport(path)


def wordCount(text):
 
    words = text.split()
    count = len(words)
    return count


def getText(path):
   
    with open(path) as f:
        return f.read()
    print()


def charCount(text):
   
    text = text.lower()
    charDict = dict()
    for i in text:
            if i.isalpha() and i not in charDict:
                 charDict[i] = 1
            elif i.isalpha() and i in charDict:
                 charDict[i] += 1 
    return charDict


def getReport(path):
   
     book = getText(path)
     wc = wordCount(book)
     charDict = charCount(book)
     charOut = charSort(charDict)
     print(f"--- Begin report of {path} ---")
     print(f"{wc} words found in the document\n")
     for i in charOut:
          print(f"the \'{i['char']}\' character was found {i['num']} times")
     print("--- End report ---")


def listMake(dict):
    
     out = []
     for i in dict:
          out.append({'char':i, 'num':dict[i]})
     return out


def sortFunc(dict):
     
     return dict['num']

          
def charSort(chars):
     
     newList=listMake(chars)
     newList.sort(reverse=True, key=sortFunc)
     return newList


main()
