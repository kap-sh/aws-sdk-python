"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "ALL_PERSONALLY_IDENTIFIABLE_INFORMATION",
    "NUMBERS",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_PERSONALLY_IDENTIFIABLE_INFORMATION",
        "NUMBERS",
        "CUSTOM",
    )
)


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
