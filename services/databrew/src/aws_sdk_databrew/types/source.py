"""Generated from Smithy shape ``com.amazonaws.databrew#Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

Source: TypeAlias = Literal[
    "S3",
    "DATA-CATALOG",
    "DATABASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "DATA-CATALOG",
        "DATABASE",
    )
)


def serialize_json(value: Source) -> str:
    return value


def deserialize_json(data: str) -> Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Source value: {data!r}")
    return cast(Source, data)
