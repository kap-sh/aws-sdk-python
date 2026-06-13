"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationAwsServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_aws_service

RecommendationAwsServiceList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationAwsServiceList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendationAwsServiceList:
    return list(data)
