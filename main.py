def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = words_count(file_contents)
    print(file_contents)
    print (f"word count = {word_count}")
    print (f"character count = {char_count(file_contents)}")

def words_count(file_contents):
    words= file_contents.split()
    return len(words)

def char_count(file_contents):
    char_counter= {}
    for char in file_contents.lower():
        if char.isalnum():
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1
    return char_counter



main() 