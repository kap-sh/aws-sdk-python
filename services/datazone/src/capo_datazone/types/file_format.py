"""Generated from Smithy shape ``com.amazonaws.datazone#FileFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The file format for a notebook export in Amazon SageMaker Unified Studio.</p>"""
FileFormat: TypeAlias = Literal[
    "PDF",
    "IPYNB",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileFormat) -> str:
    return value


def deserialize_json(data: str) -> FileFormat:
    return cast(FileFormat, data)
