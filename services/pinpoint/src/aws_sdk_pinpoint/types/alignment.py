"""Generated from Smithy shape ``com.amazonaws.pinpoint#Alignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Alignment: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEFT",
        "CENTER",
        "RIGHT",
    )
)


def serialize_json(value: Alignment) -> str:
    return value


def deserialize_json(data: str) -> Alignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Alignment value: {data!r}")
    return cast(Alignment, data)
