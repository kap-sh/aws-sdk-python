"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AIRecommendationInstanceType: TypeAlias = Literal[
    "ml.g5.xlarge",
    "ml.g5.2xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.48xlarge",
    "ml.g6.xlarge",
    "ml.g6.2xlarge",
    "ml.g6.4xlarge",
    "ml.g6.8xlarge",
    "ml.g6.12xlarge",
    "ml.g6.16xlarge",
    "ml.g6.24xlarge",
    "ml.g6.48xlarge",
    "ml.g6e.xlarge",
    "ml.g6e.2xlarge",
    "ml.g6e.4xlarge",
    "ml.g6e.8xlarge",
    "ml.g6e.12xlarge",
    "ml.g6e.16xlarge",
    "ml.g6e.24xlarge",
    "ml.g6e.48xlarge",
    "ml.g7e.2xlarge",
    "ml.g7e.4xlarge",
    "ml.g7e.8xlarge",
    "ml.g7e.12xlarge",
    "ml.g7e.24xlarge",
    "ml.g7e.48xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3.16xlarge",
    "ml.p4d.24xlarge",
    "ml.p4de.24xlarge",
    "ml.p5.4xlarge",
    "ml.p5.48xlarge",
    "ml.p5e.48xlarge",
    "ml.p5en.48xlarge",
    "ml.p6-b200.48xlarge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ml.g5.xlarge",
        "ml.g5.2xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.48xlarge",
        "ml.g6.xlarge",
        "ml.g6.2xlarge",
        "ml.g6.4xlarge",
        "ml.g6.8xlarge",
        "ml.g6.12xlarge",
        "ml.g6.16xlarge",
        "ml.g6.24xlarge",
        "ml.g6.48xlarge",
        "ml.g6e.xlarge",
        "ml.g6e.2xlarge",
        "ml.g6e.4xlarge",
        "ml.g6e.8xlarge",
        "ml.g6e.12xlarge",
        "ml.g6e.16xlarge",
        "ml.g6e.24xlarge",
        "ml.g6e.48xlarge",
        "ml.g7e.2xlarge",
        "ml.g7e.4xlarge",
        "ml.g7e.8xlarge",
        "ml.g7e.12xlarge",
        "ml.g7e.24xlarge",
        "ml.g7e.48xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3.16xlarge",
        "ml.p4d.24xlarge",
        "ml.p4de.24xlarge",
        "ml.p5.4xlarge",
        "ml.p5.48xlarge",
        "ml.p5e.48xlarge",
        "ml.p5en.48xlarge",
        "ml.p6-b200.48xlarge",
    )
)


def serialize_aws_json_1_1(value: AIRecommendationInstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationInstanceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AIRecommendationInstanceType value: {data!r}"
        )
    return cast(AIRecommendationInstanceType, data)
