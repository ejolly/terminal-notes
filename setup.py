from setuptools import setup

setup(
    name="note",
    version="0.1",
    py_modules=["note"],
    install_requires=["Click",],
    entry_points="""
        [console_scripts]
        note=note:note_writer
    """,
)
