import re

from Token import Token, DICT_TOKENS
import Error


def verifyBracket(tokens, line):
    flag = 0
    for elem in tokens:
        if elem.receiveTypeToken() == "BRACKET":
            flag += 1
        if elem.receiveTypeToken() == "BRACKET_BACK":
            flag -= 1
    if flag != 0:
        raise Error.ErrorBracket(")", line)


def verifyFigureBracket(tokens, line):
    flag = 0
    for elem in tokens:
        if elem.receiveTypeToken() == "FIGURE_BRACKET":
            flag += 1
        if elem.receiveTypeToken() == "FIGURE_BRACKET_BACK":
            flag -= 1
    if flag != 0:
        raise Error.ErrorFigureBracket("}", line)


class Lex:

    def __init__(self, kod):
        self.kod = kod
        self.lexemes_lines = list()

    def analise(self):
        for ii in range(len(self.kod)):

            lexemes = list()
            words = self.kod[ii].split()
            for j in range(len(words)):
                lexemes.append(self.find_token(words[j], ii + 1, j + 1))
                if lexemes[0].receiveTypeToken() == "INT":
                    raise Error.ErrorStartLine(lexemes[0].receiveValue(), j + 1)
            verifyBracket(lexemes, ii + 1)
            verifyFigureBracket(lexemes, ii + 1)
            self.lexemes_lines.append(lexemes)

    def find_token(self, word, num_line, num):

        for elem in DICT_TOKENS:
            result = re.search(DICT_TOKENS[elem], word)
            if result:
                return Token(elem, word, num_line, num)
        raise Error.ErrorSyn(word, num_line, num)

    def show(self):
        for ii in range(len(self.lexemes_lines)):
            for elem in self.lexemes_lines[ii]:
                elem.toString()

    def get(self):
        return self.lexemes_lines


