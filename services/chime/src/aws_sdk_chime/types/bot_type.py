"""Generated from Smithy shape ``com.amazonaws.chime#BotType``."""

from typing import Literal, TypeAlias, cast

BotType: TypeAlias = Literal["ChatBot",]


# --- restJson1 ser/de ---
def serialize_json(value: BotType) -> str:
    return value


def deserialize_json(data: str) -> BotType:
    return cast(BotType, data)
