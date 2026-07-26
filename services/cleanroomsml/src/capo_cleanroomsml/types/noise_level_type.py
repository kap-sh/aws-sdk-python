"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#NoiseLevelType``."""

from typing import Literal, TypeAlias, cast

NoiseLevelType: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NoiseLevelType) -> str:
    return value


def deserialize_json(data: str) -> NoiseLevelType:
    return cast(NoiseLevelType, data)
