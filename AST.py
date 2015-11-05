
class Node(object):

    def __str__(self):
        return self.printTree()


class BinExpr(Node):

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Program(Node):

    def __init__(self, blocks):
        self.blocks = blocks

class Blocks(Node):

    def __init__(self, block, blocks):
        self.block = block
        self.blocks = blocks


class Init(Node):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

class Declarations(Node):
    def __init__(self, declarations, declaration):
        self.declarations = declarations
        self.declaration = declaration

class Declaration(Node):
    def __init__(self, type, inits, error):
        self.type = type
        self.inits = inits
        self.error = error

class Inits(Node):
    def __init__(self, inits, init ):
        self.inits = inits
        self.init = init

class Instructions(Node):
     def __init__(self, instructions, instruction):
         self.instructions = instructions
         self.instruction = instruction

class Condition(Node):
    pass


class Expression(Condition):
    pass

class Instruction(Node):
    pass

class Print(Instruction):
    def __init__(self, expression, error):
        self.expression = expression
        self.error = error

class Labeled(Instruction):
    def __init__(self, id, instruction):
        self.id = id
        self.instruction = instruction

class Assignment(Instruction):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

class Choice(Instruction):
    def __init__(self, _if, _else):
        self._if = _if
        self._else = _else

class If(Node):
    def __init__(self, cond, statement, error):
        self.cond = cond
        self.statement = statement
        self.error = error

class Else(Node):
    def __init__(self, statement):
        self.statement = statement

class Const(Node):
    pass
    #...

class Integer(Const):
    pass
    #...


class Float(Const):
    pass
    #...


class String(Const):
    pass
    #...


class Variable(Node):
    pass
    #...




# ...

