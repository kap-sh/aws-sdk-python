"""Generated from Smithy shape ``com.amazonaws.connect#LexBotsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.lex_bot

LexBotsList: TypeAlias = list["aws_sdk_connect.types.lex_bot.LexBot"]


# --- restJson1 ser/de ---
def serialize_json(value: LexBotsList) -> list:
    import aws_sdk_connect.types.lex_bot

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.lex_bot.serialize_json(item))
    return out


def deserialize_json(data: list) -> LexBotsList:
    import aws_sdk_connect.types.lex_bot

    out: LexBotsList = []
    for item in data:
        out.append(aws_sdk_connect.types.lex_bot.deserialize_json(item))
    return out
