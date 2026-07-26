"""Generated from Smithy shape ``com.amazonaws.connect#LexBotsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.lex_bot

LexBotsList: TypeAlias = list["capo_connect.types.lex_bot.LexBot"]


# --- restJson1 ser/de ---
def serialize_json(value: LexBotsList) -> list:
    import capo_connect.types.lex_bot

    out: list = []
    for item in value:
        out.append(capo_connect.types.lex_bot.serialize_json(item))
    return out


def deserialize_json(data: list) -> LexBotsList:
    import capo_connect.types.lex_bot

    out: LexBotsList = []
    for item in data:
        out.append(capo_connect.types.lex_bot.deserialize_json(item))
    return out
