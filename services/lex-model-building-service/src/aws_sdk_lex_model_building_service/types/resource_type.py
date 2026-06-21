"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "BOT",
    "INTENT",
    "SLOT_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
