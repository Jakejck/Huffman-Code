
# Problem 3 explanation :

### Design

Used data  structure: huffman_tree
Because we need involve huffman_tree to encode and decode data.

### Time complexities

Time complexities is O(n2+nlog(n)) because that each character in input string will spend n time to match its respondent huffman binary codes and the .sort() function used in the create_huffman_tree() function

### Space complexities

Space complexities is O(2n) because we need store input string and the set of char_frequency and codes.

Note : n means the number of character.
