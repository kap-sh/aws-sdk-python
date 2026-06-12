"""Generated from Smithy shape ``com.amazonaws.costexplorer#RecommendationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.recommendation_id

RecommendationIdList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.recommendation_id.RecommendationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationIdList:
    return list(data)
