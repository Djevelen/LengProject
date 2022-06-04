from Lex import Lex
from Abstract_Sin_Tr import appointNode, OperationNode, WhileNode, IfNode, LinkedListNode, PrintNode, LinkedListOperatioinNode
import Error


class Pars:

    def __init__(self, kod):
        self.kod = kod
        self.node_list = list()

    def parse(self):

        for ii in range(len(self.kod)):
            line = self.kod[ii]

            if line[-1].receiveTypeToken() != "SEMICOLON":
                raise Error.ErrorSemicolon(ii + 1)

            if line[0].receiveTypeToken() == "VAR" and line[1].receiveTypeToken() == "ASSIGNMENT":
                self.node_list.append(self.setAssign(line))
            elif line[0].receiveTypeToken() == "PRINT_TRIGGER":
                self.node_list.append(self.setPrint(line))
            elif line[0].receiveTypeToken() == "IF_TRIGGER":
                self.node_list.append(self.setIf(line))
            elif line[0].receiveTypeToken() == "WHILE_TRIGGER":
                self.node_list.append(self.setWhile(line))
            elif line[0].receiveTypeToken() == "LINKED_LIST_TRIGGER":
                self.node_list.append(self.setLinkedList(line))
            elif line[1].receiveTypeToken() == "LL_INSERT_END":
                self.node_list.append(self.setLLInsertAtEnd(line))

            elif line[1].receiveTypeToken() == "LL_INSERT_HEAD":

                self.node_list.append(self.setLLInsertAtHead(line))
            elif line[1].receiveTypeToken() == "LL_DELETE":

                self.node_list.append(self.setLLDelete(line))
            elif line[1].receiveTypeToken() == "LL_DELETE_HEAD":

                self.node_list.append(self.setLLDeleteAtHead(line))
            elif line[1].receiveTypeToken() == "LL_SEARCH":

                self.node_list.append(self.setLLSearch(line))
            elif line[1].receiveTypeToken() == "LL_IS_EMPTY":

                self.node_list.append(self.setLLIsEmpty(line))
            else:
                raise Error.ErrorKod(line[1].receiveValue(), ii + 1)
        return self.node_list

    def setAssign(self, line):
        name_variable = line[0].receiveValue()
        value = line[2:len(line)-1]
        if len(value) == 1:
            type_token = value[0].receiveTypeToken()
            if type_token == "INT":
                return appointNode("Assign", name_variable, value, type_token)
            if type_token == "VAR":
                return appointNode("Assign", name_variable, value, type_token)
        else:
            if len(value) == 3:
                return appointNode("Assign", name_variable, self.setOperation(value), "Operation")
            else:
                return appointNode("Assign", name_variable, self.setOperation(value), "OperationHard")

    def setPrint(self, line):
        value = line[2:len(line)-2]
        if len(value) == 1:
            type_value = value[0].receiveTypeToken()
            if type_value == "INT":
                return PrintNode("Print", int(value), type_value)
            elif type_value == "VAR":
                return PrintNode("Print", value, type_value)

            else:
                pass
        else:
            pass

    def setIf(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.receiveValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.receiveValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.receiveValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.receiveValue() == "}":
                    flag = 5
                    continue

                line_kod.append(elem)
                if elem.receiveValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        for line in loop:
            if line[0].receiveTypeToken() == "VAR" and line[1].receiveTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].receiveTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")


        return IfNode("If", condition, ready_loop)

    def setWhile(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.receiveValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.receiveValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.receiveValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.receiveValue() == "}":
                    flag = 5
                    continue

                line_kod.append(elem)
                if elem.receiveValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()

        for line in loop:
            if line[0].receiveTypeToken() == "VAR" and line[1].receiveTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].receiveTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")


        return WhileNode("While", condition, ready_loop)

    def setOperation(self, value):
        if len(value) == 3:
            left_operand = value[0]
            sign = value[1]
            right_operand = value[2]
            return OperationNode("Operation", left_operand, right_operand, sign, final=True)
        else:
            condition = [elem.receiveValue() for elem in value]
            return OperationNode("Operation", value, None, None, final=False)

    def setLinkedList(self, line):
        name_linked_list = line[1].receiveValue()
        values = line[4:len(line)-2]
        new_values = list()
        for elem in values:
            if elem.receiveTypeToken() != "VIRGULE":
                new_values.append(elem)
        return LinkedListNode("LinkedList", name_linked_list, new_values)

    def setLLInsertAtEnd(self, line):
        name_variable = line[0].receiveValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtEnd", name_variable, value)

    def setLLInsertAtHead(self, line):
        name_variable = line[0].receiveValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtHead", name_variable, value)

    def setLLDelete(self, line):
        name_variable = line[0].receiveValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDelete", name_variable, value)

    def setLLDeleteAtHead(self, line):
        name_variable = line[0].receiveValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDeleteAtHead", name_variable, None)

    def setLLSearch(self, line):
        name_variable = line[0].receiveValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLSearch", name_variable, value)

    def setLLIsEmpty(self, line):
        name_variable = line[0].receiveValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLIsEmpty", name_variable, None)

    def receiveNodeList(self):
        return self.node_list







