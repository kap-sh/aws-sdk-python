"""Generated from Smithy shape ``com.amazonaws.quicksight#FileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FileFormat: TypeAlias = Literal[
    "CSV",
    "TSV",
    "CLF",
    "ELF",
    "XLSX",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "TSV",
        "CLF",
        "ELF",
        "XLSX",
        "JSON",
    )
)


def serialize_json(value: FileFormat) -> str:
    return value


def deserialize_json(data: str) -> FileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileFormat value: {data!r}")
    return cast(FileFormat, data)
