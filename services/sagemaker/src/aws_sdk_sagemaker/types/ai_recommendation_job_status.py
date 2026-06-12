"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AIRecommendationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: AIRecommendationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AIRecommendationJobStatus value: {data!r}")
    return cast(AIRecommendationJobStatus, data)
