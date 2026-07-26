"""Generated from Smithy shape ``com.amazonaws.quicksight#FileFormat``."""

from typing import Literal, TypeAlias, cast

FileFormat: TypeAlias = Literal[
    "CSV",
    "TSV",
    "CLF",
    "ELF",
    "XLSX",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileFormat) -> str:
    return value


def deserialize_json(data: str) -> FileFormat:
    return cast(FileFormat, data)
