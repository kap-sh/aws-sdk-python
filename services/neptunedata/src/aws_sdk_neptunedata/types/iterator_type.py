"""Generated from Smithy shape ``com.amazonaws.neptunedata#IteratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

IteratorType: TypeAlias = Literal[
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
    "TRIM_HORIZON",
    "LATEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AT_SEQUENCE_NUMBER",
        "AFTER_SEQUENCE_NUMBER",
        "TRIM_HORIZON",
        "LATEST",
    )
)


def serialize_json(value: IteratorType) -> str:
    return value


def deserialize_json(data: str) -> IteratorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IteratorType value: {data!r}")
    return cast(IteratorType, data)
