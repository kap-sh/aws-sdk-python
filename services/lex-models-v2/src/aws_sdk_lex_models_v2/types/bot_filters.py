"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_filter

BotFilters: TypeAlias = list["aws_sdk_lex_models_v2.types.bot_filter.BotFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: BotFilters) -> list:
    import aws_sdk_lex_models_v2.types.bot_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.bot_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotFilters:
    import aws_sdk_lex_models_v2.types.bot_filter

    out: BotFilters = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.bot_filter.deserialize_json(item))
    return out
