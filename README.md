# ownJSON
_Little json parser_


## How to install
```
git clone https://github.com/Perchinka/ownJSON.git
cd ownJSON
pip3 install pytest 
pytest .
```
---

## How to use
Without flag **-p** it will validate json from files or stdin

```bash
python3 main.py -h

usage: main.py [-h] [-f FILE] [-p] [json]

Validate JSON

positional arguments:
  json                  JSON string to validate (default: None)

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  JSON file to validate (default: None)
  -p, --parse           Parse JSON string (default: False)
``` 
---

## Contributing
It does not have a wide functionality, but if you want to modify it, then you can safely fork :D

- Fork the repository.
- Create a new branch for your feature/fix: `git checkout -b feature-name`
- Make your changes.
- Commit your changes: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature-name`
- Submit a pull request.
