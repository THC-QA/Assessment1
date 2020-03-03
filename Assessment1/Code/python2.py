#!/usr/bin/env python3
def one(input1, input2):
	if len(input1) > len(input2):
		return input1
	elif len(input1) < len(input2):
		return input2
	else:
		return input1 + " " + input2
def two(string):
	string = string.lower().split("bert")
	out = ""
	if len(string) == 3:
		out += string[1]
	return out
def three(arg1):
	if arg1%3 == 0 and arg1%5 == 0:
		return "fizzbuzz"
	elif arg1%3 == 0:
		return "fizz"
	elif arg1%5 == 0:
		return "buzz"
	else:
		return "null"
def four(string):
    out = []
    string = string.split()
    for n in string:
        int_n = []
        for char in n:
            int_n.append(int(char))
        out.append(sum(int_n))
    return max(out)
def five(string):
    string = string.split(",")
    string = [string[x:x+4] for x in range(0,len(string),4)]
    out = []
    for l in range(len(string)):
        if string[l][1] == "private.key":
            if string[l][2] == "False":
                out.append(string[l][0])
    return list(set(out))
def six(string):
	if "ie" in string:
		if "cie" in string:
			return False
		else:
			return True
	if "ei" in string:
		if "cei" in string:
			return True
		else:
			return False
def seven(string):
	string = string.lower()
	vowels = ("a","e","i","o","u")
	count = 0
	for ch in string:
		if ch in vowels:
			count += 1
	return count
def eight(num):
	seed = 1
	for i in range (1,num+1):
		seed *= i
	return seed
def nine(string, char):
    string = string.split()
    string = "".join(string)
    for ch in string:
        if ch == char:
            return string.index(ch) + 1
    return -1
def ten(string, num, char):
	string = "".join(string.lower().split())
	if len(string) < num:
		return False
	elif string[num-1] == char:
		return True
	else:
		return False