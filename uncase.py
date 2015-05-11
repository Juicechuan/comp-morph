# uncase the (already tolkenized) data
import codecs

infile = open('corpus.txt')
with codecs.open("corpus_lower.txt", "w", "utf-8-sig") as outfile:
   for line in infile:
     outfile.write(line.decode('utf-8').lower())
infile.close()
