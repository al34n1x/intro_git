#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def get_name(names_ranks):
  return names_ranks[0]
  
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  year = ''
  rank = ''
  name = ''
  list_res = []
  dict_names_ranks = {}
  f = open(filename, 'r')
  string_of_the_whole_file = f.read()
  
  #extract the year and print it
  match_year = re.search(r'\"center\">Popularity in \d+', string_of_the_whole_file)
 
  if match_year:
    year = match_year.group()[23:]
    print('year found:', year)
  else:
    print('year not found')
    
  #extract the names and its respective ranks and print them
  names_boys_ranks = re.findall(r'(<td>\d+)(</td><td>\w+)', string_of_the_whole_file) #me devuelve una lista de tuples de la forma [(ranking1,nombre_niño1),...]
  names_girls_ranks = re.findall(r'(<td>\d+)(^\D</td><td>\w+)', string_of_the_whole_file) #me devuelve una lista de tuples de la forma [(ranking1,nombre_niña1),...]
  print('La lista de niñas es:', names_girls_ranks)
  for i in range(len(names_boys_ranks)):
    name_boy = names_boys_ranks[i][1][9:]
    rank = names_boys_ranks[i][0][4:]
    #diccionario que contiene claves igual a los nombres niño y valor igual al ranking correspondiente para esos nombres
    dict_names_ranks[name_boy] = rank
    print('name of the boy and his rank found:', name_boy + ' ' + rank )
    #dar vuelta el orden de cada tuple en las listas de niños
    names_boys_ranks[i] = names_boys_ranks[i][::-1]
  for i in range(len(names_girls_ranks)):
    name_girl = names_girls_ranks[i][1][10:]
    rank = names_girls_ranks[i][0][4:]
    #diccionario que contiene claves igual a los nombres niña y valor igual al ranking correspondiente para esos nombres
    dict_names_ranks[name_girl] = rank
    print('name of the girl and her rank found:', name_girl + ' ' + rank)
    #dar vuelta el orden de cada tuple en las listas de niñas
    names_girls_ranks[i] = names_girls_ranks[i][::-1]

  #ordenar por orden alfabético de nombres
  names_boys_ranks = sorted(names_boys_ranks, key = get_name)
  names_girls_ranks = sorted(names_girls_ranks, key = get_name)
  
  #creo la lista resultado list_res con ambas listas y la ordeno
  list_res = names_boys_ranks + names_girls_ranks
  list_res = sorted(list_res, key = get_name)

  #convierto la lista de tuples (name,rank) a una lista de strings 'name rank'
  for i in range(len(list_res)):
    list_res[i] = ' '.join(list_res[i])
    
  #a la lista de strings ordenada alfabéticamente le agrego el año adelante
  if year != '':
    list_res = list_res.insert(0, year)
    
  #imprimo el diccionario 
  print('El diccionario con los nombres es el siguiente:', dict_names_ranks)
  
  #imprimo la lista [year, 'name rank', ... ]
  print('La lista resultado solicitada es la siguiente:', list_res)
  
  f.close()
  
  return list_res


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary == False:
    for i in range(len(args)):
      lista = extract_names(args[i])
      print('La lista resultado del main es:', lista)
  else:
    for i in range(len(args)): 
      for str in extract_names(args[i]):
        summaryfile.write(str)
        summaryfile.write(' ')   
      summaryfile.write('\n')      
               
if __name__ == '__main__':
  main()
