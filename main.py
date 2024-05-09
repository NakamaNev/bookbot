def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = words_count(file_contents)
    print(file_contents)
    print (f"word count= {word_count}")

def words_count(file_contents):
    words= file_contents.split()
    return len(words)



main() 