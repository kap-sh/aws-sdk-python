"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_analyzer_recommendation

BotAnalyzerRecommendationList: TypeAlias = list[
    "capo_lex_models_v2.types.bot_analyzer_recommendation.BotAnalyzerRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerRecommendationList) -> list:
    import capo_lex_models_v2.types.bot_analyzer_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.bot_analyzer_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotAnalyzerRecommendationList:
    import capo_lex_models_v2.types.bot_analyzer_recommendation

    out: BotAnalyzerRecommendationList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.bot_analyzer_recommendation.deserialize_json(item)
        )
    return out
