import sys
sys.path.append('../json_parser')

import pytest
from ownparser import Parser
from ownlexer import Lexer

parser = Parser()

def test_should_raise_exception_when_wrong_brackets_parring():
    with pytest.raises(Exception):
        parser.parse(Lexer().lex('{"a": "hello"'))
        parser.parse(Lexer().lex('{"a": "hello"}}'))
        parser.parse(Lexer().lex('{"a": "hello"}]'))
        parser.parse(Lexer().lex('{"a": "hello"}['))
        parser.parse(Lexer().lex('{"a": "hello"}{'))
    
def test_should_return_dict_with_list():
    assert parser.parse(Lexer().lex('{"a": ["hello", "world"]}'))[0] == {"a": ["hello", "world"]}

def test_should_return_dict_with_dict():
    assert parser.parse(Lexer().lex('{"a": {"b": "hello"}}'))[0] == {"a": {"b": "hello"}}

def test_should_return_dict_with_number():
    assert parser.parse(Lexer().lex('{"a": 1}'))[0] == {"a": 1}

def test_should_return_dict_with_string():
    assert parser.parse(Lexer().lex('{"a": "hello"}'))[0] == {"a": "hello"}

def test_should_return_dict_with_bool():
    assert parser.parse(Lexer().lex('{"a": true}'))[0] == {"a": True}
    assert parser.parse(Lexer().lex('{"a": false}'))[0] == {"a": False}

def test_should_return_dict_with_null():
    assert parser.parse(Lexer().lex('{"a": null}'))[0] == {"a": None}

def test_should_return_list_with_dict():
    assert parser.parse(Lexer().lex('[{"a": "hello"}]'))[0] == [{"a": "hello"}]

def test_should_return_list_with_list():
    assert parser.parse(Lexer().lex('[["a", "hello"]]'))[0] == [["a", "hello"]]
