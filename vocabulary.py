from random import randint
import requests, bs4

my_words = {
        'dubious' : 'doubtful',
        'fret' : 'to worry',
        'erie' : 'strange or frightening',
        'artisan' : 'someone good at making things by hand',
        'abstain' : 'restrain yourself from doing something fun'
}

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
  print("Sshh: " + q)
  r = requests.get('https://www.merriam-webster.com/dictionary/' + q)
  html = bs4.BeautifulSoup(r.text, "lxml")
  ce = html.select('.cite-example')
  # we could randomize the sentence
  print (len(ce))
  if len(ce) == 0:
    return get_definition(index)
  sent_index = randint(0, (len(ce)-1))
  print("index: " + str(sent_index))
  print("sentence: " + ce[sent_index].getText())
  fill_in_the_blank = ce[sent_index].getText().replace(q, '__________')
  return (q, fill_in_the_blank)
        
if __name__ == "__main__":
  print("Hello Owen, ready to start the test?")
  while( len(my_words.keys()) != 0):
    index = randint(0, (len(my_words.keys())-1)) 
    #word, definition = get_definition(index)
    word, definition = get_sentence(index)
    print("What word means: " + definition)
    answer = input()
    if answer == word:
      print('Good Job!')
      del my_words[answer] #correct_answers.append(index)
      print(my_words)
#		if answer in my_words:
#			if my_words[answer] == definition:
#				print('Good Job!')
#				del my_words[answer] #correct_answers.append(index)
#				print(my_words)
#			else:
#				print("Ugh!")
    else:
      print("Nope")

