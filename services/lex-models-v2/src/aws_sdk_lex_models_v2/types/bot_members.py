"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_member

BotMembers: TypeAlias = list["aws_sdk_lex_models_v2.types.bot_member.BotMember"]


# --- restJson1 ser/de ---
def serialize_json(value: BotMembers) -> list:
    import aws_sdk_lex_models_v2.types.bot_member

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.bot_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotMembers:
    import aws_sdk_lex_models_v2.types.bot_member

    out: BotMembers = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.bot_member.deserialize_json(item))
    return out
