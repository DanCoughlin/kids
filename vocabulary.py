from random import randint
import requests, bs4

'''
my_words = {
  'dubious' : 'doubtful',
  'fret' : 'to worry',
  'erie' : 'strange or frightening',
  'artisan' : 'someone good at making things by hand',
  'abstain' : 'restrain yourself from doing something fun'
}
'''

my_words = {}

def get_word(index):
  counter = 0
  for k,v in my_words.items():
    if counter == index:
      return k
    counter += 1


def get_definition(index):
  q = get_word(index)
  return (q, my_words[q])
  
            
def get_sentence(index):
  q = get_word(index) 
  r = requests.get('https://www.merriam-webster.com/dictionary/' + q)
  html = bs4.BeautifulSoup(r.text, "lxml")
  ce = html.select('.cite-example')
  
  if len(ce) == 0:
    return get_definition(index)
  sent_index = randint(0, (len(ce)-1))
  fill_in_the_blank = ce[sent_index].getText().replace(q, '__________')
  return (q, fill_in_the_blank)


def get_question():        
    index = randint(0, (len(my_words.keys())-1)) 
    question_type = randint(0, 1)
    if question_type == 0: 
      word, definition = get_definition(index)
    else:
      word, definition = get_sentence(index)
    return (word, definition)


if __name__ == "__main__":
  print("Hello Owen, ready to start the test?")
  print('Choose the word that best fits the definition or completes the sentence.')
  file = open('words.txt')
  for lines in file:
    l = lines.split(':')
    word = l[0].strip()
    definition = l[1].strip()
    my_words[word] = definition

  while( len(my_words.keys()) != 0):
    (word, question) = get_question()
    print(question)
    answer = input()
    if answer == word:
      print('Good Job!')
      del my_words[answer] #correct_answers.append(index)
      #print(my_words)
    else:
      print("Nope")

