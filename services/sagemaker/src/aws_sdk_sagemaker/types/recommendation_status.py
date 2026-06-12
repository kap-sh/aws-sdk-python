"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RecommendationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "NOT_APPLICABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "NOT_APPLICABLE",
    )
)


def serialize_aws_json_1_1(value: RecommendationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
