"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RecommendationSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.recommendation_summary

RecommendationSummariesList: TypeAlias = list[
    "capo_cost_optimization_hub.types.recommendation_summary.RecommendationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSummariesList) -> list:
    import capo_cost_optimization_hub.types.recommendation_summary

    out: list = []
    for item in value:
        out.append(
            capo_cost_optimization_hub.types.recommendation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationSummariesList:
    import capo_cost_optimization_hub.types.recommendation_summary

    out: RecommendationSummariesList = []
    for item in data:
        out.append(
            capo_cost_optimization_hub.types.recommendation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
