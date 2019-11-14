#coding=utf-8
file = open("europarl.fr", 'r')
file_out = open("europarl.fr_ST", 'w')
vocab_file = open("fr.vocab")

word_set = set()
for line in vocab_file.readlines():
    word = line.strip()
    if word not in word_set:
        word_set.add(word)


for line in file.readlines():
    words = line.strip().split()
    new_sen = []
    for id, word in enumerate(words):
        if word.startswith("l\'") or word.startswith("n\'") or word.startswith("s\'") or word.startswith("c\'") \
                or word.startswith("d\'") or word.startswith("l\’"):
            word = word = word[0:2] + " " + word[2:]

        if word.startswith("qu\'"):
            word = word = word[0:3] + " " + word[3:]
        if word == "du":
            word = "de le"
        if word == "des":
            word = "de les"
        if word.startswith("\"") and not word.endswith("\""):
            word = word[1:]
        if word.startswith("\'") and not word.endswith("\'"):
            word = word[1:]
        if not word.startswith("\'") and word.endswith("\'"):
            word = word[:-1]
        if not word.startswith("\"") and word.endswith("\""):
            word = word[:-1]
        if word.endswith("'ll") or word.endswith("'ve"):
            word = word[:-3] + " " + word[-3:]
        if word.endswith("'t") or word.endswith("'m") or word.endswith("'s"):
            word = word[:-2] + " " + word[-2:]
        if word.endswith("%"):
            word = word[:-1] + " " + word[-1]
        if word.startswith("("):
            word = word[0] + " " + word[1:]
        if word.endswith(",") or word.endswith(".") or word.endswith("?") or word.endswith(")") or word.endswith(":"):
            if len(word) > 2:
                word = word[:-1] + " " + word[-1]

        new_sen.append(word)
    new_sentence = " ".join(new_sen)
    words = new_sentence.split()

    for id, word in enumerate(words):
        this_line = []
        this_line.append(str(id+1))
        this_line.append(word)
        for i in range(13):
            this_line.append('_')
        if id == 0:
            this_line[12] = 'Y'
        file_out.write("\t".join(this_line))
        file_out.write('\n')
    file_out.write('\n')
