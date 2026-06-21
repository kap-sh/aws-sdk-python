"""Generated from Smithy shape ``com.amazonaws.iot#ThingIndexingMode``."""

from typing import Literal, TypeAlias, cast

ThingIndexingMode: TypeAlias = Literal[
    "OFF",
    "REGISTRY",
    "REGISTRY_AND_SHADOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingIndexingMode:
    return cast(ThingIndexingMode, data)
