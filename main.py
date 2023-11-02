from ownjson import is_valid
import argparse 
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate JSON', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('json', nargs='?' ,type=str, help='JSON string to validate')
    parser.add_argument('-f', '--file', type=str, help='JSON file to validate')
    parser.add_argument('-p', '--parse', action='store_true', help='Parse JSON string')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            json_string = f.read()
    elif args.json:
        json_string = args.json
    else:
        json_string = sys.stdin.read() 

    if args.parse:
        from ownjson import from_string
        print(from_string(json_string))
    else:
        print(is_valid(json_string))