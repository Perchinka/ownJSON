from ownlexer import Lexer

class Parser:
    def parse(self, tokens):
        if tokens[0] == '{':
            return self.parse_object(tokens[1:])
        elif tokens[0] == '[':
            return self.parse_list(tokens[1:])
        else:
            return tokens[0], tokens[1:]
    
    def parse_object(self, tokens: list):
        obj = {}
        
        if tokens[0] == '}':
            return obj, tokens[1:]
        
        while True:
            key = tokens[0]
            if type(key) is str:
                tokens = tokens[1:]
            else:
                raise Exception('Expected string as key, got {}'.format(key))
            
            if tokens[0] != ':':
                raise Exception('Expected colon, got {}'.format(tokens[2]))
            
            value, tokens = self.parse(tokens[1:])
            obj[key] = value

            if tokens[0] == '}':
                return obj, tokens[1:]
            elif tokens[0] == ',':
                tokens = tokens[1:]
            else:
                raise Exception('Expected comma or end of object, got {}'.format(tokens[0]))
                
    def parse_list(self, tokens: list):
        arr = []

        if tokens[0] == ']':
            return arr, tokens[1:]
        
        while True:
            value, tokens = self.parse(tokens)
            arr.append(value)
            
            if tokens[0] == ']':
                return arr, tokens[1:]
            elif tokens[0] == ',':
                tokens = tokens[1:]
            else:
                raise Exception('Expected comma or end of array, got {}'.format(tokens[0]))
            

def from_string(json_string: str):
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.lex(json_string)
    parsed, _ = parser.parse(tokens)
    return parsed
