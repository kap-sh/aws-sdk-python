"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RecommendationJobType: TypeAlias = Literal[
    "Default",
    "Advanced",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "Advanced",
    )
)


def serialize_aws_json_1_1(value: RecommendationJobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationJobType value: {data!r}")
    return cast(RecommendationJobType, data)
