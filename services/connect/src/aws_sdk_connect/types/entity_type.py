"""Generated from Smithy shape ``com.amazonaws.connect#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "USER",
    "AI_AGENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    return cast(EntityType, data)
