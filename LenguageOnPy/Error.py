def errorMessage(message):
    return f"\033[31m {message}"


class ErrorSyn(Exception):

    def __init__(self, data, line, position):
        self.data = str(data)
        self.line = line
        self.position = position

    def __str__(self):
        text = f"Неизвестный символ в {self.line} строке, на " \
               f"{self.position} позиции: {self.data}"
        return errorMessage(text)


class ErrorKod(Exception):

    def __init__(self, data, line):
        self.data = str(data)
        self.line = line

    def __str__(self):
        text = f"Неизвестная конструкция в {self.line} строке"
        return errorMessage(text)


class ErrorSymbol(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f'Не хватает символа "{self.data}" в {self.line} строке'
        return errorMessage(text)


class ErrorSemicolon(ErrorSymbol):

    def __init__(self, line):
        data = ";"
        super().__init__(data, line)


class ErrorBracket(ErrorSymbol):

    def __init__(self, data, line):
        super().__init__(data, line)


class ErrorFigureBracket(ErrorSymbol):

    def __init__(self, data, line):
        super().__init__(data, line)


class ErrorStartLine(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f"Не корректное значение в начале {self.line} строки: {self.data}"
        return errorMessage(text)
