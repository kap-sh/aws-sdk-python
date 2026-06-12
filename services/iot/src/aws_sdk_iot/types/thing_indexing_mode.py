"""Generated from Smithy shape ``com.amazonaws.iot#ThingIndexingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ThingIndexingMode: TypeAlias = Literal[
    "OFF",
    "REGISTRY",
    "REGISTRY_AND_SHADOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "REGISTRY",
        "REGISTRY_AND_SHADOW",
    )
)


def serialize_json(value: ThingIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingIndexingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThingIndexingMode value: {data!r}")
    return cast(ThingIndexingMode, data)
