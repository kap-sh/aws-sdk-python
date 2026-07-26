"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotType``."""

from typing import Literal, TypeAlias, cast

BotType: TypeAlias = Literal[
    "Bot",
    "BotNetwork",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotType) -> str:
    return value


def deserialize_json(data: str) -> BotType:
    return cast(BotType, data)
