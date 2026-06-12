"""Generated from Smithy shape ``com.amazonaws.connect#ContactInteractionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactInteractionType: TypeAlias = Literal[
    "AGENT",
    "AUTOMATED",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "AUTOMATED",
        "CUSTOMER",
    )
)


def serialize_json(value: ContactInteractionType) -> str:
    return value


def deserialize_json(data: str) -> ContactInteractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactInteractionType value: {data!r}")
    return cast(ContactInteractionType, data)
