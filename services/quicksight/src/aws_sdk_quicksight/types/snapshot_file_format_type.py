"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SnapshotFileFormatType: TypeAlias = Literal[
    "CSV",
    "PDF",
    "EXCEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "PDF",
        "EXCEL",
    )
)


def serialize_json(value: SnapshotFileFormatType) -> str:
    return value


def deserialize_json(data: str) -> SnapshotFileFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotFileFormatType value: {data!r}")
    return cast(SnapshotFileFormatType, data)
