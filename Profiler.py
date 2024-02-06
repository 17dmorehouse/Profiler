  """Load a text file as a list.

   Arguments:
   -text file name (and directory path, if needed)

   Exceptions:
   -IOError if filename not found.

   Returns:
   -A list of all words in a text file in lower case.

   Requires-import sys

   """
import time
start_time = time.time()   
   
import sys

def load(file):
       """Open a text file & return a list of lowercase strings."""
       try:
           with open(file) as in_file:
               loaded_txt = in_file.read().strip().split('\n')
               loaded_txt = [x.lower() for x in loaded_txt]
               return loaded_txt
       except IOError as e:
           print("{}\nError opening {}. Terminating program.".format(e, file),
               file=sys.stderr)
           sys.exit(1)
           
word_list = load("C:/Users/dev46/OneDrive/Desktop/School Documents/Spring 2024/Statistics of Big Data/Data/dictionary.txt")
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

# print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
# print(*pali_list, sep='\n')

def find_palingrams():
       """Find dictionary palingrams."""
       pali_list = []
       for word in word_list:
           end = len(word)
           rev_word = word[::-1]
           if end > 1:
               for i in range(end):
                   if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                       pali_list.append((word, rev_word[end-i:]))
                   if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                       pali_list.append((rev_word[:end-i], word))
       return pali_list

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
    
end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))

start_time = time.time()   
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))


