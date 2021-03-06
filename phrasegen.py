import random

MIN_WORD_LENGTH = 8
MAX_WORD_LENGTH = 99
PHRASE_LENGTH = 4

print("Reading words...")
with open("corncob_lowercase.txt", "r") as corncob:
	words = [x.strip() for x in corncob.readlines()]
totalWordCount = len(words)
print("Read", totalWordCount, "words.")

print("Deleting words shorter than", str(MIN_WORD_LENGTH), "or longer than", str(MAX_WORD_LENGTH) + "...")
words = [word for word in words if len(word) >= MIN_WORD_LENGTH and len(word) <= MAX_WORD_LENGTH]
print("Deleted", totalWordCount - len(words), "words (word count is now", str(len(words)) + ").\n")

if len(words) < 1:
	print("No words matched the given conditions.")
	exit()

while True:
	for _ in range(PHRASE_LENGTH):
		print(random.choice(words), end=" ")
	input()
