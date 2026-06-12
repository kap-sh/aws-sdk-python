"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.rightsizing_recommendation

RightsizingRecommendationList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.rightsizing_recommendation.RightsizingRecommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendationList) -> list:
    import aws_sdk_cost_explorer.types.rightsizing_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.rightsizing_recommendation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RightsizingRecommendationList:
    import aws_sdk_cost_explorer.types.rightsizing_recommendation

    out: RightsizingRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.rightsizing_recommendation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
