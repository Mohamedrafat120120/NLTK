import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


class NLP_task():
    # def __init__(self,Sentence) -> None:
    #     self.Sentence=Sentence

    def Option1(self, Sentence):
        tokenize_word = word_tokenize(Sentence)
        return tokenize_word

    def Option2(self, Sentence):
        tokenize_sentence = sent_tokenize(Sentence)
        return tokenize_sentence

    def Option3(self, Sentence):
        sent_split = Sentence.split('#')
        return sent_split


nltk.download('punkt')

Sentence = input("Enter a sentence: ")
option1 = 'word_tokenization'
option2 = 'sentence_tokenization'
option3 = 'split_function'
print('option1->', option1, "or", 'option2->',
      option2, "or", 'option3->', option3)

user_choice = input('Choose your option:')

if user_choice == '1' or 'option1':
    print(NLP_task().Option1(Sentence))
elif user_choice == '2' or 'option2':
    print(NLP_task().Option2(Sentence))
elif user_choice == '3' or 'option3':
    print(NLP_task().Option3(Sentence))
else:
    print('error::please check your option')
