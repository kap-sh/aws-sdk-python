"""Generated from Smithy shape ``com.amazonaws.appflow#FileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

FileType: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
        "PARQUET",
    )
)


def serialize_json(value: FileType) -> str:
    return value


def deserialize_json(data: str) -> FileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileType value: {data!r}")
    return cast(FileType, data)
