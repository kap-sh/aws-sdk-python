"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_filter

BotLocaleFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_locale_filter.BotLocaleFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleFilters) -> list:
    import aws_sdk_lex_models_v2.types.bot_locale_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.bot_locale_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotLocaleFilters:
    import aws_sdk_lex_models_v2.types.bot_locale_filter

    out: BotLocaleFilters = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.bot_locale_filter.deserialize_json(item))
    return out
