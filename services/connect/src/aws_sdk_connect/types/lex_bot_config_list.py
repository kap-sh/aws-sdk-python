"""Generated from Smithy shape ``com.amazonaws.connect#LexBotConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.lex_bot_config

LexBotConfigList: TypeAlias = list["aws_sdk_connect.types.lex_bot_config.LexBotConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: LexBotConfigList) -> list:
    import aws_sdk_connect.types.lex_bot_config

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.lex_bot_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> LexBotConfigList:
    import aws_sdk_connect.types.lex_bot_config

    out: LexBotConfigList = []
    for item in data:
        out.append(aws_sdk_connect.types.lex_bot_config.deserialize_json(item))
    return out
