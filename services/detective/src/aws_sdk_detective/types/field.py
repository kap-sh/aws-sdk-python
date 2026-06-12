"""Generated from Smithy shape ``com.amazonaws.detective#Field``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

Field: TypeAlias = Literal[
    "SEVERITY",
    "STATUS",
    "CREATED_TIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEVERITY",
        "STATUS",
        "CREATED_TIME",
    )
)


def serialize_json(value: Field) -> str:
    return value


def deserialize_json(data: str) -> Field:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Field value: {data!r}")
    return cast(Field, data)
