import sys
from scanner import Scanner


class Interpreter:
    def __init__(self) -> None:
        self.had_error = False

    def run_file(self, filename):
        with open(filename, encoding='utf-8') as file:
            self.run(file.read())
            if self.had_error:
                exit()

    def run_prompt(self):
        for line in sys.stdin:
            self.run(line)
            if self.had_error:
                self.had_error = False

    def run(self, source):
        scanner = Scanner(source)
        tokens, errors = scanner.scan_tokens()
        for error in errors:
            self.error(*error)
        for token in tokens:
            print(token)

    def error(self, line: int, message):
        self.report(line, "", message)

    def report(self, line: int, where, message):
        print(f'line: {line}, error: {where} {message}')
        self.had_error = True


if __name__ == '__main__':
    interp = Interpreter()
    interp.run_file('new.txt')