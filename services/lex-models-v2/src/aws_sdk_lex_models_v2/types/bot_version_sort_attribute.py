"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionSortAttribute``."""

from typing import Literal, TypeAlias, cast

BotVersionSortAttribute: TypeAlias = Literal["BotVersion",]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotVersionSortAttribute:
    return cast(BotVersionSortAttribute, data)
