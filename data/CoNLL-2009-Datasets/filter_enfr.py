en_file = open('europarl-v7.fr-en.en', 'r')
en_out = open('europarl.en','w')
fr_file = open('europarl-v7.fr-en.fr', 'r')
fr_out = open('europarl.fr','w')

idx = 0
for line_en, line_fr in zip(en_file.readlines(), fr_file.readlines()):
    len_en = len(line_en.split())
    len_fr = len(line_fr.split())
    if len_en < 10:
        continue
    if len_fr < 10:
        continue
    en_out.write(line_en)
    fr_out.write(line_fr)
    idx +=1


print idx
