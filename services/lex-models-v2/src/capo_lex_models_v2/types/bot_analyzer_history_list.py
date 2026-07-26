"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_analyzer_history_summary

BotAnalyzerHistoryList: TypeAlias = list[
    "capo_lex_models_v2.types.bot_analyzer_history_summary.BotAnalyzerHistorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerHistoryList) -> list:
    import capo_lex_models_v2.types.bot_analyzer_history_summary

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.bot_analyzer_history_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotAnalyzerHistoryList:
    import capo_lex_models_v2.types.bot_analyzer_history_summary

    out: BotAnalyzerHistoryList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.bot_analyzer_history_summary.deserialize_json(item)
        )
    return out
