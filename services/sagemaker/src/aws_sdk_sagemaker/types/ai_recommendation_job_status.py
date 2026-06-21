"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationJobStatus``."""

from typing import Literal, TypeAlias, cast

AIRecommendationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationJobStatus:
    return cast(AIRecommendationJobStatus, data)
