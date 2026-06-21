"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "NOT_APPLICABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
