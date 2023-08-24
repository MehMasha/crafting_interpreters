class Token:
    def __init__(self, t_type, lexeme, literal, line):
        self.t_type = t_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f'{self.t_type} {self.lexeme} {self.literal}'