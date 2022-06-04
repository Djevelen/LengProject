from Lex import Lex
from Pars import Pars
from Interpret import Interpret

Cat_1 = ["a = ( 5 + 3 * ( 5 - 3 ) - 2 ) * 2 - 17 ; ",
         "PRINT ( a ) ;",
         "b = 20 / a ;",
         "PRINT ( b ) ;",
         "WHILE ( a < 5 ) { a = a + 1 ; PRINT ( a ) ; } ;",
         "IF ( 22 > b ) { PRINT ( b ) ; } ;",
         ]

Cat_2 = ["LinkedList link_list = { 1 , 3 , 4 } ;",
         "link_list .insertAtEnd ( 2 ) ;",
         "link_list .insertAtHead ( 1 ) ;",
         "link_list .delete ( 2 ) ;",
         "link_list .deleteAtHead ( ) ;",
         "link_list .search ( 2 ) ;",
         "link_list .isEmpty ( ) ;"
        ]


def receivekod():
    cat = list()
    while True:
        line = input("Введите строку кода: ")
        if line:
            cat.append(line)
        else:
            break
    print(f"Введено строк: {len(cat)}\n")
    return cat


def main():
    # Вводим новый код
    # cat = get_cat()

    lexer = Lex(Cat_1)  # Выполняется поиск лексем

    # print(cat)  # Показывается весь список cats
    lexer.analise()  # Тут происходит анализ всех лексем

    lexemes = lexer.get()  # А тут создаётся список всех лексем
    # lexer.show()  # Выводятся всек лексемы

    parser = Pars(lexemes)  # Здесь выводятся объекты для парсинга(лексемы)

    parser.parse()  # Начало парсинга для поиска записей
    node_list = parser.receiveNodeList()  # Список записей

    inter = Interpret(node_list)  # Объект для выполнения

    inter.execute()  # Начало вычполнения

    # print(inter.linkedlist_values)  # Показывает ВСЕ переменные
    # print(inter.variables_values)  # Показывает все LinkedList Переменные


if __name__ == '__main__':
    main()
