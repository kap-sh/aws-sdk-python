"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotSortAttribute``."""

from typing import Literal, TypeAlias, cast

BotSortAttribute: TypeAlias = Literal["BotName",]


# --- restJson1 ser/de ---
def serialize_json(value: BotSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotSortAttribute:
    return cast(BotSortAttribute, data)
