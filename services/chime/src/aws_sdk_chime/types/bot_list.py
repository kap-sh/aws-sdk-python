"""Generated from Smithy shape ``com.amazonaws.chime#BotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.bot

BotList: TypeAlias = list["aws_sdk_chime.types.bot.Bot"]


# --- restJson1 ser/de ---
def serialize_json(value: BotList) -> list:
    import aws_sdk_chime.types.bot

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.bot.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotList:
    import aws_sdk_chime.types.bot

    out: BotList = []
    for item in data:
        out.append(aws_sdk_chime.types.bot.deserialize_json(item))
    return out
