with open("story.txt", "r") as f:  # reading the file story.txt
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# for loop to check for tags, locates words
# enumaerate gives access to position and element at that positicaton
for i, char in enumerate(story): 
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1


#ask users to give a value for each word
answers = {} #empty dictionary

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#replace instances of our word
for word in words:
    story = story.replace(word, answers[word])

print(story)



