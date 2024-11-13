# Shehadi Fino
# UWYO COSC 1010
# 11-12-24
# HW 04
# Lab Section:14
# Sources, people worked with, help given to: Ryan
# Your
# Comments
# Here

with open("prompt.txt", "r") as input_file, open("out.txt", "w") as output_file:
    for line in input_file:
        pairs = line.strip().split("\t")
        output_line = ""
        for pair in pairs:
            key, value = pair.split(":")
            count = int(value)
            if key == "w":
                output_line += " " * count
            elif key == "*":
                output_line += "*" * count
        output_file.write(output_line + "\n")