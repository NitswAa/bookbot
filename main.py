def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_count = {}
    for word in text.split():
        word = word.lower()
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_dict(d):
    return dict(sorted(d.items(), key = lambda x:x[1], reverse=True))

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

if __name__ == "__main__":
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    sorted_count = sort_dict(count_letters(file_contents))
    wc = count_words(file_contents)
    print("--- Book Report ---")
    print(f"Words: {wc}\n")
    for kv in sorted_count.items():
        if 'a' <= kv[0] and kv[0] <= 'z':
            print(f"The '{kv[0]}' character was found {kv[1]} times.")

