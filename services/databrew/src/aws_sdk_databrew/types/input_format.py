"""Generated from Smithy shape ``com.amazonaws.databrew#InputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

InputFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
    "EXCEL",
    "ORC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
        "PARQUET",
        "EXCEL",
        "ORC",
    )
)


def serialize_json(value: InputFormat) -> str:
    return value


def deserialize_json(data: str) -> InputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputFormat value: {data!r}")
    return cast(InputFormat, data)
