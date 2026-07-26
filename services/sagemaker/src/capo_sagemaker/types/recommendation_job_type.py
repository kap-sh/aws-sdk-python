"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobType``."""

from typing import Literal, TypeAlias, cast

RecommendationJobType: TypeAlias = Literal[
    "Default",
    "Advanced",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobType:
    return cast(RecommendationJobType, data)
