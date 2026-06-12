"""Generated from Smithy shape ``com.amazonaws.rdsdata#RecordsFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds_data.errors import DeserializationError

RecordsFormatType: TypeAlias = Literal[
    "NONE",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "JSON",
    )
)


def serialize_json(value: RecordsFormatType) -> str:
    return value


def deserialize_json(data: str) -> RecordsFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordsFormatType value: {data!r}")
    return cast(RecordsFormatType, data)
