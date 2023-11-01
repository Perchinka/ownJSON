import sys
sys.path.append('../json_parser')

from ownlexer import Lexer

import pytest

lexer = Lexer()

def test_right_ints_lexing():
    assert lexer.lex('{"a": 1, "b": 123}') == ['{', 'a', ':', 1, ',', 'b', ':', 123, '}']

def test_right_float_lexing():
    assert lexer.lex('{"a": 1.0}') == ['{', 'a', ':', 1.0, '}']

def test_right_negative_nums_lexing():
    assert lexer.lex('{"a": -1.0, "b": -1123}') == ['{', 'a', ':', -1.0, ',', 'b', ':', -1123, '}']

def test_right_bool_lexing():
    assert lexer.lex('{"a": true, "b": false}') == ['{', 'a', ':', True, ',', 'b', ':', False, '}']

def test_right_null_lexing():
    assert lexer.lex('{"a": null}') == ['{', 'a', ':', None, '}']

def test_right_string_lexing():
    assert lexer.lex('{"a": "hello"}') == ['{', 'a', ':', 'hello', '}']

def test_wrong_quote_parring():
    with pytest.raises(Exception):
        lexer.lex('{"a": "hello}')