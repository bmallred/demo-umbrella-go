#!/usr/bin/python

import os

d = {}
output = ""

fileName = "coverage.out"
if os.path.isfile(fileName):
    # Read the Go coverage details
    f = open("coverage.out", "r")

    for line in f:
        target = line.split(":")[0].split("/")[-1]
      
        if target == "mode":
            continue

        if not target in d:
            d[target] = [[], [], []]

        l = int(line.split(":")[1].split(" ")[-1])
        l2 = line.split(":")[1].split(" ")[0].split(",")

        if l > 0:
            for ll in l2:
                i = ll.split(".")[0]
                if not i in d[target][0]:
                    d[target][0].append(i)
        else:
            for ll in l2:
                i = ll.split(".")[0]
                if not i in d[target][2]:
                    d[target][2].append(i)

    for key in d.keys():
        output += "{0};{1};{2};{3};\n".format(
            key,
            ",".join(str(x) for x in d[key][0]),
            ",".join(str(x) for x in d[key][1]),
            ",".join(str(x) for x in d[key][2]))

    f.close()

    # Time to write our output file.
    fileName = ".umbrella-coverage"
    if os.path.isfile(fileName):
        os.remove(fileName)

    f = open(fileName, "w")
    f.write(output)
    f.close()
