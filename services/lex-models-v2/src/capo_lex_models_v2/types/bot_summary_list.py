"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_summary

BotSummaryList: TypeAlias = list["capo_lex_models_v2.types.bot_summary.BotSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: BotSummaryList) -> list:
    import capo_lex_models_v2.types.bot_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.bot_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotSummaryList:
    import capo_lex_models_v2.types.bot_summary

    out: BotSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.bot_summary.deserialize_json(item))
    return out
