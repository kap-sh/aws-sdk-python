"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupIndexingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ThingGroupIndexingMode: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ON",
    )
)


def serialize_json(value: ThingGroupIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingGroupIndexingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThingGroupIndexingMode value: {data!r}")
    return cast(ThingGroupIndexingMode, data)
