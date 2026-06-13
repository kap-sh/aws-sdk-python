"""Generated from Smithy shape ``com.amazonaws.quicksight#FontDecoration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FontDecoration: TypeAlias = Literal[
    "UNDERLINE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNDERLINE",
        "NONE",
    )
)


def serialize_json(value: FontDecoration) -> str:
    return value


def deserialize_json(data: str) -> FontDecoration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FontDecoration value: {data!r}")
    return cast(FontDecoration, data)
