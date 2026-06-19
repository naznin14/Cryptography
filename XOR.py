'''pr1'''

string = "abcd"
result = ""

for char in string:
    xor_char = chr(ord(char) ^ 1)
    result += xor_char
print(result)
