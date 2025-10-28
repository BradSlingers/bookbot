def get_num_words(text):
    list_words = text.split()
    return len(list_words)

def get_num_chars(text):
    char_dict = {}
    for character in text.lower():
        if character in char_dict:
            char_dict[character]+= 1
        else: char_dict[character] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def convert(the_dict):
    my_list = []
    for k, val in the_dict.items():
        my_list.append({"char":k,"num" : val})
    #return my_list
    my_list.sort(reverse=True,key=sort_on)
    return my_list