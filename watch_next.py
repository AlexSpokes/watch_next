#code to compare movie description with other suitbale movies
import spacy
nlp = spacy.load('en_core_web_md')
#add description here for film e.g. Hulk
hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
model_hulk = nlp(hulk)
#open movies file and iterate through lines
with open('movies.txt', 'r') as movies:
  number = 0
  count = 0
  item = 0
  #if similarity higher than previous values, store that position
  for token in movies:
    similarity = nlp(token).similarity(model_hulk)
    if float(similarity) > number:
        number = similarity
        item = count
        count +=1
    else:
        count +=1
    print(similarity)
print(number)
print(item)
#use previously stored position to fidn best matching movie
with open('movies.txt', 'r') as movies:
    repeat = 0
    for line in movies: 
      if repeat == item:
        print("The best matched movie is " + line[0:7])
        repeat += 1
      else: 
        repeat += 1
