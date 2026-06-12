"""Generated from Smithy shape ``com.amazonaws.connect#Visibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Visibility: TypeAlias = Literal[
    "ALL",
    "ASSIGNED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ASSIGNED",
        "NONE",
    )
)


def serialize_json(value: Visibility) -> str:
    return value


def deserialize_json(data: str) -> Visibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Visibility value: {data!r}")
    return cast(Visibility, data)
