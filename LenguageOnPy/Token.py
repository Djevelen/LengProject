import re


DICT_TOKENS = {
    "LINKED_LIST_TRIGGER": r"LinkedList",
    "LL_INSERT_END": r".insertAtEnd",
    "LL_INSERT_HEAD": r".insertAtHead",
    "LL_DELETE_HEAD": r".deleteAtHead",
    "LL_DELETE": r".delete",
    "LL_SEARCH": r".search",
    "LL_IS_EMPTY": r".isEmpty",
    "VAR": r"[a-z][a-z0-9]*",
    "INT": r"0|([1-9][0-9]*)",
    "EQUALS": r"[=]{2}",
    "ASSIGNMENT": r"[=]",
    "SIGN_LESS": r"[<]",
    "SIGN_GREATER": r"[>]",
    "SEMICOLON": r";",
    "PLUS_SIGN": r"[+]",
    "MINUS_SIGN": r"[-]",
    "MULTIPLY_SIGN": r"[*]",
    "DIVIDE_SIGN": r"[/]",
    "VIRGULE": r"[,]",
    "DOT": r"[.]",
    "BRACKET": r"[(]",
    "BRACKET_BACK": r"[)]",
    "FIGURE_BRACKET": r"[{]",
    "FIGURE_BRACKET_BACK": r"[}]",
    "IF_TRIGGER": r"IF",
    "WHILE_TRIGGER": r"WHILE",
    "PRINT_TRIGGER": r"PRINT",
}


class Token:

    def __init__(self, type_token, value, number_line, position):
        self.type_token = type_token
        self.value = value
        self.number_line = number_line
        self.position = position

    def receiveTypeToken(self):
        return self.type_token

    def receiveValue(self):
        return self.value

    def receiveNumberLine(self):
        return self.number_line

    def receivePosition(self):
        return self.position

    def toString(self):
        text = f"[type: {self.type_token}, value: '{self.value}', " \
               f"number_line: {self.number_line}, position: {self.position}]"
        print(text)

