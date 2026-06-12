"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_recommendation_summary

BotRecommendationSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.bot_recommendation_summary.BotRecommendationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BotRecommendationSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.bot_recommendation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.bot_recommendation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BotRecommendationSummaryList:
    import aws_sdk_lex_models_v2.types.bot_recommendation_summary

    out: BotRecommendationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.bot_recommendation_summary.deserialize_json(
                item
            )
        )
    return out
