from Lex import Lex
from Pars import Pars


class Interpret:

    def __init__(self, node_list):
        self.node_list = node_list
        self.variables_values = dict()
        self.linkedlist_values = dict()

    def execute(self):
        for node in self.node_list:
            node_type = node.receiveTypeNode()
            if node_type == "Print":
                self.executePrint(node)
            elif node_type == "If":
                self.executeIf(node)
            elif node_type == "While":
                self.executeWhile(node)
            elif node_type == "Assign":
                self.executeAssign(node)
            elif node_type == "LinkedList":
                self.executeLinkedList(node)
            elif node_type == "LinkedListOperationNode":
                self.executeLinkedListOperation(node)
            else:
                print("ERROR")

    def executeAssign(self, node):
        name_variable = node.receiveNameVariable()
        type_value = node.receiveTypeValue()


        if type_value == "INT":
            value = node.receiveValue()[0].receiveValue()
            self.variables_values[name_variable] = value
        elif type_value == "VAR":
            # print(value)
            value = node.receiveValue()[0].receiveValue()
            self.variables_values[name_variable] = self.variables_values[value]
        elif type_value == "Operation":
            value = self.executeOperation(node.receiveValue())
            self.variables_values[name_variable] = value
        elif type_value == "OperationHard":
            value = node.receiveValue()
            values = value.receiveLeftOperand()
            value = self.executeHardOperation(value)
            self.variables_values[name_variable] = value


    def executePrint(self, node):
        type_value = node.receiveTypeValue()
        if type_value == "INT":
            value = node.receiveValue()
            print(value[0].receiveValue())
        elif type_value == "VAR":
            name_variable = node.receiveValue()[0].receiveValue()
            if name_variable in self.variables_values:
                value = self.variables_values[name_variable]
                print(value)
            else:
                print("ERROR")
        elif type_value == "Operation":
            pass
        else:
            print("ERROR")

    def executeIf(self, node):
        condition = node.receiveCondition()
        loop = node.receiveLoop()
        value_one = condition[0]
        sign = condition[1]
        value_two = condition[2]

        if value_one.receiveTypeToken() == "VAR":
            value_one_condition = self.variables_values[value_one.receiveValue()]
        else:
            value_one_condition = value_one.receiveValue()

        if value_two.receiveTypeToken() == "VAR":
            value_two_condition = self.variables_values[value_two.receiveValue()]
        else:
            value_two_condition = value_two.receiveValue()

        value_sign = sign.receiveValue()
        type_sign = sign.receiveTypeToken()
        if type_sign == "SIGN_GREATER":
            if int(value_one_condition) > int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.receiveTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

        elif type_sign == "SIGN_LESS":
            if int(value_one_condition) < int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.receiveTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

        elif type_sign == "EQUALS":
            if int(value_one_condition) == int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.receiveTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

    def executeWhile(self, node):
        while True:
            condition = node.receiveCondition()
            loop = node.receiveLoop()
            value_one = condition[0]
            sign = condition[1]
            value_two = condition[2]

            if value_one.receiveTypeToken() == "VAR":
                value_one_condition = self.variables_values[value_one.receiveValue()]
            else:
                value_one_condition = value_one.receiveValue()

            if value_two.receiveTypeToken() == "VAR":
                value_two_condition = self.variables_values[value_two.receiveValue()]
            else:
                value_two_condition = value_two.receiveValue()
            type_sign = sign.receiveTypeToken()

            if type_sign == "SIGN_GREATER":
                if int(value_one_condition) > int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.receiveTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break
            elif type_sign == "SIGN_LESS":

                if int(value_one_condition) < int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.receiveTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break
            elif type_sign == "EQUALS":
                if int(value_one_condition) == int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.receiveTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break

    def executeOperation(self, node):
        left = node.receiveLeftOperand()
        right = node.receiveRightOperand()
        if left.receiveTypeToken() == "VAR":
            left_operand = self.variables_values[left.receiveValue()]
        else:
            left_operand = left.receiveValue()

        if right.receiveTypeToken() == "VAR":
            right_operand = self.variables_values[right.receiveValue()]
        else:
            right_operand = right.receiveValue()
        sign = node.receiveSign()
        final = node.receiveFinal()
        value = 0
        if final:
            if sign.receiveTypeToken() == "PLUS_SIGN":
                value = int(left_operand) + int(right_operand)
            if sign.receiveTypeToken() == "MINUS_SIGN":
                value = int(left_operand) - int(right_operand)
            if sign.receiveTypeToken() == "MULTIPLY_SIGN":
                value = int(left_operand) * int(right_operand)
            if sign.receiveTypeToken() == "DIVIDE_SIGN":
                value = int(left_operand) / int(right_operand)
        else:
            pass
        return int(value)

    def executeHardOperation(self, node):
        values = node.receiveLeftOperand()
        exp = [elem.receiveValue() for elem in values]
        value = node.feature(exp)
        return value

    def executeLinkedList(self, node):
        name = node.receiveName()
        values = node.receiveValues()
        new_values = [elem.receiveValue() for elem in values]
        self.linkedlist_values[name] = new_values

    def executeLinkedListOperation(self, node):
        type_operation = node.receiveTypeOperation()

        if type_operation == "setLLInsertAtEnd":
            name_variable = node.receiveNameVariable()
            value = node.receiveValues()
            value_type = value.receiveTypeToken()
            value = value.receiveValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values.append(value)
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLInsertAtHead":
            name_variable = node.receiveNameVariable()
            value = node.receiveValues()
            value_type = value.receiveTypeToken()
            value = value.receiveValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values = [value] + values
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLDelete":
            name_variable = node.receiveNameVariable()
            value = node.receiveValues()
            value_type = value.receiveTypeToken()
            value = value.receiveValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(int(value))
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLDeleteAtHead":
            name_variable = node.receiveNameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(0)
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLSearch":
            name_variable = node.receiveNameVariable()
            value = node.receiveValues()
            value_type = value.receiveTypeToken()
            value = value.receiveValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                print(f"Element on position {value}: {values[int(value)]}")
            else:
                print("ERROR")

        elif type_operation == "setLLIsEmpty":
            name_variable = node.receiveNameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                if len(values) == 0:
                    print("LinkedList is empty.")
                else:
                    print("LinkedList is NOT empty.")
            else:
                print("ERROR")

        else:
            pass
