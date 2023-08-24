
class LEFT_PAREN:
    pass
class RIGHT_PAREN:
    pass
class LEFT_BRACE:
    pass
class RIGHT_BRACE:
    pass
class COMMA:
    pass
class DOT:
    pass
class MINUS:
    pass
class PLUS:
    pass
class SEMICOLON:
    pass
class SLASH:
    pass
class STAR:
    pass
class BANG:
    pass
class BANG_EQUAL:
    pass
class EQUAL:
    pass
class EQUAL_EQUAL:
    pass
class GREATER:
    pass
class GREATER_EQUAL:
    pass
class LESS:
    pass
class LESS_EQUAL:
    pass
class IDENTIFIER:
    pass
class STRING:
    pass

class NUMBER:
    pass
class AND:
    pass
class CLASS:
    pass
class ELSE:
    pass
class FALSE:
    pass
class FUN:
    pass
class FOR:
    pass
class IF:
    pass
class NIL:
    pass
class OR:
    pass
class PRINT:
    pass
class RETURN:
    pass
class SUPER:
    pass
class THIS:
    pass
class TRUE:
    pass
class VAR:
    pass
class WHILE:
    pass
class EOF:
    pass


token_type = [
    LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
    COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,

    BANG, BANG_EQUAL,
    EQUAL, EQUAL_EQUAL,
    GREATER, GREATER_EQUAL,
    LESS, LESS_EQUAL,

    IDENTIFIER, STRING, NUMBER,

    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,
    PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,

    EOF
]


