"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ResultFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

"""File format of the returned data."""
ResultFormat: TypeAlias = Literal[
    "CSV",
    "PARQUET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "PARQUET",
    )
)


def serialize_json(value: ResultFormat) -> str:
    return value


def deserialize_json(data: str) -> ResultFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResultFormat value: {data!r}")
    return cast(ResultFormat, data)
