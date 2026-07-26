"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_summary

BotAliasSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.bot_alias_summary.BotAliasSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasSummaryList) -> list:
    import capo_lex_models_v2.types.bot_alias_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.bot_alias_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BotAliasSummaryList:
    import capo_lex_models_v2.types.bot_alias_summary

    out: BotAliasSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.bot_alias_summary.deserialize_json(item))
    return out
