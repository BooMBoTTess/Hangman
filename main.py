import random
class game:
    def __init__(self, health):
        self.health = health
        self.word = ''
        self.visible = ''

    def get_word(self):
        with open('words.txt', 'r', encoding='utf-8') as f:
            self.word = random.choice(open('words.txt').readlines()).rstrip()
            self.visible = "_" * len(self.word)
        print(self.word)
    def open_letter(self, pos, letter):
        self.visible = self.visible[:pos] + letter + self.visible[pos+1:]

    def succes(self, letter):
        pos = self.word.find(letter)
        while pos != -1:
            self.open_letter(pos, letter)
            pos = self.word.find(letter, pos+1)
        print('Угадал', self.visible)

    def lose(self):
        self.health -= 1
        print(f'Не угадал осталось {self.health} жизней')



    def correct_letter(self, letter):
        if len(letter) == 1:
            return 1
        else:
            return 0
    def guess(self):
        print('word is: ', self.visible)
        letter = input()

        if self.correct_letter(letter):
            if letter in self.word:
                self.succes(letter)
            else:
                self.lose()
        else:
            print('Incorrect letter')


    def start(self):
        self.get_word()
        while (self.visible != self.word) and (self.health > 0):
            self.guess()
        if self.health > 0:
            print('Вы выйграли')
        else:
            print('Вы проиграли, правильное слово: ', self.word)
g = game(5)
g.start()