"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleSortAttribute``."""

from typing import Literal, TypeAlias, cast

BotLocaleSortAttribute: TypeAlias = Literal["BotLocaleName",]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleSortAttribute:
    return cast(BotLocaleSortAttribute, data)
