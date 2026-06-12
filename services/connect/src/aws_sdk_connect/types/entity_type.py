"""Generated from Smithy shape ``com.amazonaws.connect#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "USER",
    "AI_AGENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "AI_AGENT",
    )
)


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
