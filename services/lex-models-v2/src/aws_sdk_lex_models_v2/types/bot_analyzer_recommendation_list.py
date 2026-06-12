"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_analyzer_recommendation

BotAnalyzerRecommendationList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_analyzer_recommendation.BotAnalyzerRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerRecommendationList) -> list:
    import aws_sdk_lex_models_v2.types.bot_analyzer_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_analyzer_recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotAnalyzerRecommendationList:
    import aws_sdk_lex_models_v2.types.bot_analyzer_recommendation

    out: BotAnalyzerRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_analyzer_recommendation.deserialize_json(
                item
            )
        )
    return out
