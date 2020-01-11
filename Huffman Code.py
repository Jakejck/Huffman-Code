    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:21:41 2019

@author: jake
"""
import sys

class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
 
    def is_left(self):
        return self.father.left == self

def create_nodes(frequencies):
    return [Node(freq) for freq in frequencies]

def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


def get_huffman_codes(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


def count_frequency(input_string):
    # 用于存放字符
    char_store = []
    # 用于存放频数
    freq_store = []
 
    # 解析字符串
    for index in range(len(input_string)):
        if char_store.count(input_string[index]) > 0:
            temp = int(freq_store[char_store.index(input_string[index])])
            temp = temp + 1
            freq_store[char_store.index(input_string[index])] = temp
        else:
            char_store.append(input_string[index])
            freq_store.append(1)
    # 返回字符列表和频数列表
    return char_store, freq_store


def get_char_frequency(char_store=[], freq_store=[]):
    # 用于存放char_frequency
    char_frequency = []
    for item in zip(char_store, freq_store):
        temp = (item[0], item[1])
        char_frequency.append(temp)
    return char_frequency

def huffman_encoding(input_string):
    
    if  len(input_string) == 0:
        return "No data to encode!"
    else:
        char_store,freq_store = count_frequency(input_string)
        char_frequency = get_char_frequency(char_store,freq_store)
        nodes = create_nodes(freq_store)
        root = create_huffman_tree(nodes)
        codes = get_huffman_codes(nodes, root)
        encode = ''
        for index in range(len(input_string)):
            for item in zip(char_frequency,codes):
                if input_string[index] == item[0][0]:
                    encode = encode +item[1] + '/'
        return encode,char_frequency,codes

def huffman_decoding(encoded_input_string,char_frequency,codes):
    
    decode = ''
    
    encode_list = encoded_input_string.split('/')[0:-1]
    
    for x in encode_list :
        
        for item in zip(char_frequency,codes):
            
            if x == item[1]:
                decode =decode + item[0][0]
                
    return decode


"""
test the code
"""


"""
first case
"""

if __name__ == "__main__":
    
    a_great_sentence = "It's a challenge task"
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data,char_frequency,codes = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data,char_frequency,codes)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
"""
second case
"""

if __name__ == "__main__":
    a_great_sentence = "aaaaaaaa"
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data,char_frequency,codes = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data,char_frequency,codes)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


"""
third case
"""
if __name__ == "__main__":
    
    a_great_sentence = ""
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    print(huffman_encoding(a_great_sentence))
    
    
    
    
    
    
