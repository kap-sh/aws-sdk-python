"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_summary

BotLocaleSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_locale_summary.BotLocaleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.bot_locale_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.bot_locale_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotLocaleSummaryList:
    import aws_sdk_lex_models_v2.types.bot_locale_summary

    out: BotLocaleSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_locale_summary.deserialize_json(item)
        )
    return out
