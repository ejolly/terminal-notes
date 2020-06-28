#!/Users/Esh/anaconda3/bin/python
"""
Easily store and view recent notes
"""

import os
import click


@click.command()
@click.argument("note", nargs=-1)
@click.option("-a", "archive", type=int, help="Archive a specific note by its number")
@click.option("-A", "archive_all", is_flag=True, help="Archive all notes")
def note_writer(archive, archive_all, note):
    """Add or show (no args) notes"""
    if not note:
        with open("/Users/Esh/Documents/.click_notes.txt", "r") as f:
            lines = f.readlines()
        if not isinstance(archive, int) and not archive_all:
            if lines:
                click.echo("📌 You were doing...")
                for i, line in enumerate(lines):
                    print(f"{i}) {line}", end="")
        else:
            with open("/Users/Esh/Documents/.click_notes.txt", "w") as f:
                if isinstance(archive, int):
                    for i, line in enumerate(lines):
                        if i != int(archive):
                            f.write(line)
                elif archive_all:
                    f.truncate()
                    click.echo("All notes cleared!")
    else:
        with open("/Users/Esh/Documents/.click_notes.txt", "a") as f:
            to_write = f"{' '.join(note)}\n"
            f.write(to_write)


if __name__ == "__main__":
    note_writer()
