"""Generated from Smithy shape ``com.amazonaws.finspacedata#ExportFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Data View Export File Format"""
ExportFileFormat: TypeAlias = Literal[
    "PARQUET",
    "DELIMITED_TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARQUET",
        "DELIMITED_TEXT",
    )
)


def serialize_json(value: ExportFileFormat) -> str:
    return value


def deserialize_json(data: str) -> ExportFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFileFormat value: {data!r}")
    return cast(ExportFileFormat, data)
