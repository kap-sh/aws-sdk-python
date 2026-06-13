"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.recommendation

RecommendationList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.recommendation.Recommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationList) -> list:
    import aws_sdk_cost_optimization_hub.types.recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationList:
    import aws_sdk_cost_optimization_hub.types.recommendation

    out: RecommendationList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
