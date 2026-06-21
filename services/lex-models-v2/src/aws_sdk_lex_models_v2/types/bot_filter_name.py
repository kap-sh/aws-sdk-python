"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilterName``."""

from typing import Literal, TypeAlias, cast

BotFilterName: TypeAlias = Literal[
    "BotName",
    "BotType",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotFilterName) -> str:
    return value


def deserialize_json(data: str) -> BotFilterName:
    return cast(BotFilterName, data)
