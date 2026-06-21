"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupIndexingMode``."""

from typing import Literal, TypeAlias, cast

ThingGroupIndexingMode: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingGroupIndexingMode:
    return cast(ThingGroupIndexingMode, data)
