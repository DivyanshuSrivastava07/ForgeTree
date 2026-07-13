from pathlib import Path

from .parser import Parser
from .builder import Builder
from .writer import FileSystemWriter


class ForgeTree:
    """
    High-level API for generating project structures.
    """

    def __init__(self) -> None:
        self.parser = Parser()
        self.builder = Builder()
        self.writer = FileSystemWriter()

    def generate(
        self,
        text: str,
        destination: str | Path,
    ) -> None:
        """
            Generate the project structure on disk.
        """

        nodes = self.parser.parse(text)

        roots = self.builder.build(nodes)

        self.writer.write(
            roots,
            destination,
        )


def generate(
    text: str,
    destination: str | Path,
) -> None:
    """
    Generate a project directory structure from an indented text description.

    Parameters
    ----------
    text : str
        The directory structure written as an indented string.

    destination : str | Path
        The destination directory where the project structure
        will be created.
    """

    ForgeTree().generate(
        text,
        destination,
    )