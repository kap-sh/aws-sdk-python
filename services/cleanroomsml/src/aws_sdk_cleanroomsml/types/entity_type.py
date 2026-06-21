"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "ALL_PERSONALLY_IDENTIFIABLE_INFORMATION",
    "NUMBERS",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    return cast(EntityType, data)
