"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ReferenceType``."""

from typing import Literal, TypeAlias, cast

ReferenceType: TypeAlias = Literal[
    "Intent",
    "Bot",
    "BotAlias",
    "BotChannel",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceType:
    return cast(ReferenceType, data)
