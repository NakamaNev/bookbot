def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = words_count(file_contents)
    char_count_dict = char_count(file_contents)
    sorted_char_counts = sort_char_counts(char_count_dict)
    report = [
        f"--- Begin report of books/frankenstein.txt ---",
        f"{word_count} words found in the document",]
    
    for char, count in sorted_char_counts:
        report.append(f"The '{char}' character was found {count} times")
    
    print(file_contents)
    for line in report:
        print(line)

    print ("--- End report ---")
    
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

def sort_char_counts(char_count_dict):
  char_count_list = list(char_count_dict.items())
  char_count_list.sort(key=lambda x: (-x[1], x[0])) 

  return char_count_list



main() 