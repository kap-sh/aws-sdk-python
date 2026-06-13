"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#NoiseLevelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

NoiseLevelType: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "MEDIUM",
        "LOW",
        "NONE",
    )
)


def serialize_json(value: NoiseLevelType) -> str:
    return value


def deserialize_json(data: str) -> NoiseLevelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NoiseLevelType value: {data!r}")
    return cast(NoiseLevelType, data)
