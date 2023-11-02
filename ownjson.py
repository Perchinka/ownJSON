from ownlexer import Lexer
from ownparser import Parser


def from_string(json_string: str):
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.lex(json_string)
    parsed, _ = parser.parse(tokens)
    return parsed

def is_valid(json_string: str):
    try:
        from_string(json_string)
        return True
    except Exception as e:
        return e