"""Generated from Smithy shape ``com.amazonaws.chime#BotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.bot

BotList: TypeAlias = list["capo_chime.types.bot.Bot"]


# --- restJson1 ser/de ---
def serialize_json(value: BotList) -> list:
    import capo_chime.types.bot

    out: list = []
    for item in value:
        out.append(capo_chime.types.bot.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotList:
    import capo_chime.types.bot

    out: BotList = []
    for item in data:
        out.append(capo_chime.types.bot.deserialize_json(item))
    return out
