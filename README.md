# Note.py

Super simple command line program for managing "what you were working on" style notes in the terminal.  
Inspired by [doing](https://github.com/ttscoff/doing) but even simpler.  
Uses the [click](https://click.palletsprojects.com/en/7.x/) Python library and is specifically setup to make the `note` command available to your shell following [these directions](https://click.palletsprojects.com/en/7.x/setuptools/)  
**Note:** There is no "archive" function. Removing a note always _deletes_ it from storage!  

## Usage

Type `note --help` to see usage options

## Auto prompt of pending items on new terminal launch

Add `note` to your `.zlogin` (or equivalent) so the cmd program gets added to PATH and auto-executes when a new terminal is created. This is will print nothing or pending items if they exist. 
