infile = open("project_twitter_data.csv", "r")
datafile = open("resulting_data.csv", "w")
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
              

def pos_count(astring):
    i = 0
    astring = strip_punctuation(astring)
    newstring = astring.split()
    for word in newstring:
        for posword in positive_words:
            if word == posword:
                i += 1
    return i

def neg_count(astring):
    i = 0
    astring = strip_punctuation(astring)
    newstring = astring.split()
    for word in newstring:
        for negword in negative_words:
            if word == negword:
                i += 1
    return i

def strip_punctuation(astring):
    for c in astring:
        if c in punctuation_chars:
            astring = astring.replace(c, "")
    return astring


def writedata(datafile):
    datafile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    datafile.write("\n")
    lines = infile.readlines()
    real = lines[1:]
    print(real)
    headeroff = lines.pop(0)
    for x in real:
        lst = x.strip().split(",")
        datafile.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], pos_count(lst[0]), neg_count(lst[0]), pos_count(lst[0]) - neg_count(lst[0])))
        datafile.write("\n")

writedata(datafile)
infile.close()
datafile.close()


