# Advent of Code
# Day 1
# https://adventofcode.com/2023/day/1


file = open("input.txt", "r")
input = file.readlines()

numbers = []
for line in input:
    number = 0
    last_digit = 0
    first = False
    for chr in line:
        if chr.isdigit():
            if first == False:
                number = int(chr) * 10
                first = True
            last_digit = int(chr)
    number += last_digit
    numbers.append(number)

total = 0
for i in numbers:
    total += i
print("First Puzzle:", total)

numbers = []
for line in input:
    number = 0
    last_digit = 0

    str3 = ""
    str4 = ""
    str5 = ""
    first = False
    for chr in line:
        if chr.isdigit():
            if first == False:
                number = int(chr) * 10
                first = True
            last_digit = int(chr)
        else:
            str3 = str3 + chr
            if len(str3) > 3:
                str3 = str3[1:4]
            str4 = str4 + chr
            if len(str4) > 4:
                str4 = str4[1:5]
            str5 = str5 + chr
            if len(str5) > 5:
                str5 = str5[1:6]

            num = 0
            if str3 == "one":
                str3 = ""
                num = 1
            elif str3 == "two":
                str3 = ""
                num = 2
            elif str3 == "six":
                str3 = ""
                num = 6
            if str4 == "four":
                str4 = ""
                num = 4
            elif str4 == "five":
                str4 = ""
                num = 5
            elif str4 == "nine":
                str4 = ""
                num = 9
            if str5 == "three":
                str5 = ""
                num = 3
            elif str5 == "seven":
                str5 = ""
                num = 7
            elif str5 == "eight":
                str5 = ""
                num = 8
            
            if num != 0:
                if first == False:
                    number = num * 10
                    first = True
                else:
                    last_digit = num
    number += last_digit
    numbers.append(number)

total = 0
for i in numbers:
    total += i
print("Second Puzzle:", total)
