"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_summary

BotVersionSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_version_summary.BotVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.bot_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.bot_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotVersionSummaryList:
    import aws_sdk_lex_models_v2.types.bot_version_summary

    out: BotVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_version_summary.deserialize_json(item)
        )
    return out
