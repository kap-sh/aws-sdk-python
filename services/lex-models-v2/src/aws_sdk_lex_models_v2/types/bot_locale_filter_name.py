"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilterName``."""

from typing import Literal, TypeAlias, cast

BotLocaleFilterName: TypeAlias = Literal["BotLocaleName",]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleFilterName) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleFilterName:
    return cast(BotLocaleFilterName, data)
