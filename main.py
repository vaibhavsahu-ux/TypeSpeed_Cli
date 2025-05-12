import random
import time

# sentences to type

sentences = [
        "the quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "OpenAI develops advanced AI models.",
        "Practice daily to improve your typing speed."
    ]

text_to_type = random.choice(sentences)
print("Type the following sentence:\n")
print(text_to_type)

# taking input from the user

input("\nPress enter to start")
start_time = time.time()

typed_text = input("\nStart typing:\n")
end_time = time.time()

elapsed_time =  end_time - start_time
print(f"\nTime taken: {elapsed_time:.2f} seconds")

# calculating wpm

word_count = len(typed_text.split())
wpm = (word_count / elapsed_time) * 60

# calculating accuracy

correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(text_to_type) and c == text_to_type[i])
accuracy = (correct_chars / len(text_to_type)) * 100

print(f"WPM: {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")


