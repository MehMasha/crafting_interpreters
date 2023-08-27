from tokens_types import *
from tokens import Token


class Scanner:
    def __init__(self, source) -> None:
        self.source = source
        self.tokens = []
        self.errors = []
        self.start = 0
        self.current = 0
        self.line = 1

    def is_at_end(self):
        return self.current >= len(self.source) - 1

    def scan_tokens(self):
        while not self.is_at_end():
            print()
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(EOF, "", None, self.line));
        return self.tokens, self.errors

    def scan_token(self):
        char = self.get_advance()
        match char:
            case '(': self.add_token(LEFT_PAREN)
            case ')': self.add_token(RIGHT_PAREN)
            case '{': self.add_token(LEFT_BRACE)
            case '}': self.add_token(RIGHT_BRACE)
            case ',': self.add_token(COMMA)
            case '.': self.add_token(DOT)
            case '-': self.add_token(MINUS)
            case '+': self.add_token(PLUS)
            case ';': self.add_token(SEMICOLON)
            case '*': self.add_token(STAR)
            case '!': 
                self.add_token(BANG_EQUAL if self.match('=') else BANG)
            case '=': 
                self.add_token(EQUAL_EQUAL if self.match('=') else EQUAL)
            case '<': 
                self.add_token(LESS_EQUAL if self.match('=') else LESS)
            case '>': 
                self.add_token(GREATER_EQUAL if self.match('=') else GREATER)
            case '/':
                if self.match('/'):
                    while self.get_peek() != '\n' and not self.is_at_end():
                        self.get_advance()
                else:
                    self.add_token(SLASH)
            case ' ': pass
            case '\r': pass
            case '\t': pass
            case '\n':
                self.line += 1
            case '"':
                self.is_string()
            case _:
                if char.isdigit():
                    self.is_number()
                elif self.is_alpha(char):
                    self.is_identifier()
                else:
                    self.errors.append((self.line, 'Это что за закорючка?'))

    def match(self, expected):
        if self.is_at_end():
            return False;
        if self.source[self.current] != expected:
            return False;

        self.current += 1;
        return True;

    def add_token(self, t_type):
        self.add_token_literal(t_type, None)

    def add_token_literal(self, t_type, literal):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(t_type, text, literal, self.line))

    def get_advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def get_peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def is_string(self):
        while self.get_peek() != '"' and not self.is_at_end():
            if self.get_peek() == '\n':
                self.line += 1
            self.get_advance()

        if self.is_at_end():
            self.errors(self.line, 'А строку и не закрыл')
            return

        self.get_advance()

        value = self.source[self.start + 1:self.current - 1]
        self.add_token_literal(STRING, value)

    def is_number(self):
        while self.get_peek().isdigit():
            self.get_advance()

        next_char = self.get_peek()
        if next_char == '.' and self.peek_next().isdigit():
            self.get_advance()
            while self.get_peek().isdigit():
                self.get_advance()

        self.add_token_literal(NUMBER, float(self.source[self.start:self.current]))

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]
    
    def is_identifier(self):
        while self.is_alpha_num(self.get_peek()):
            self.get_advance()

        text = self.source[self.start:self.current]
        if text in identifier_types:
            self.add_token(identifier_types[text])
        else:
            self.add_token(IDENTIFIER)

    def is_alpha(self, char):
        return char.isalpha() or char == '_' 
    def is_alpha_num(self, char):
        return char.isalpha() or char == '_' or char.isdigit()
