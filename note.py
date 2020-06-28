#!/Users/Esh/anaconda3/bin/python
"""
Easily store and view recent notes
"""

from pathlib import Path
import click


@click.command()
@click.argument("note", nargs=-1)
@click.option("-f", "filepath", is_flag=True, help="Print location to notes file")
@click.option(
    "-a",
    "-d",
    "archive",
    type=int,
    help="Remove a specific note by its number (0 indexed)",
)
@click.option(
    "-e", "edit", type=int, help="Edit a specific note by its number (0 indexed)"
)
@click.option("-A", "archive_all", is_flag=True, help="Remove all notes")
def note_writer(archive, archive_all, note, filepath, edit):
    """Simple program to add or show notes from a file. Works entirely through command flags. Removed notes are deleted from the file so there is no history of completed items!"""

    p = Path.home() / ".click_notes.txt"
    if not p.exists():
        print("No notes file found...creating")
        p.touch()

    # If -f is passed just print the location to the file and exit
    if filepath:
        click.echo(f"Notes file is here: {p.absolute()}")
        return

    # Otherwise always read the notes file first
    with open(p, "r") as f:
        lines = f.readlines()

    # If no note text is passed and no archival flags are provided just print all notes
    if not note:
        if not isinstance(archive, int) and not archive_all:
            if lines:
                click.echo("📌 You were doing...")
                for i, line in enumerate(lines):
                    print(f"{i}) {line}", end="")
        # If no note text is passed but archival flags are passed, remove the requested lines
        else:
            with open(p, "w") as f:
                if isinstance(archive, int):
                    for i, line in enumerate(lines):
                        if i != int(archive):
                            f.write(line)
                elif archive_all:
                    f.truncate()
                    click.echo("All notes cleared!")
    # If the edit flag is passed rewrite that specific line
    else:
        to_write = f"{' '.join(note)}\n"
        if isinstance(edit, int):
            with open(p, "w") as f:
                for i, line in enumerate(lines):
                    if i == int(edit):
                        f.write(to_write)
                    else:
                        f.write(line)
        # Otherwise just append to the end of the file
        else:
            with open(p, "a") as f:
                f.write(to_write)


if __name__ == "__main__":
    note_writer()
