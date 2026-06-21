"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIRecommendationJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListAIRecommendationJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIRecommendationJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAIRecommendationJobsSortBy:
    return cast(ListAIRecommendationJobsSortBy, data)
