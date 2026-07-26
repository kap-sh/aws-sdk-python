"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationJobStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "STOPPING",
    "STOPPED",
    "DELETING",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobStatus:
    return cast(RecommendationJobStatus, data)
