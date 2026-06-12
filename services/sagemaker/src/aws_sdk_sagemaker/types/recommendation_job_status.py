"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "STOPPING",
        "STOPPED",
        "DELETING",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: RecommendationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationJobStatus value: {data!r}")
    return cast(RecommendationJobStatus, data)
