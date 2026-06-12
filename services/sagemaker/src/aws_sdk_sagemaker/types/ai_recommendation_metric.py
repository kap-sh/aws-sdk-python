"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AIRecommendationMetric: TypeAlias = Literal[
    "ttft-ms",
    "throughput",
    "cost",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ttft-ms",
        "throughput",
        "cost",
    )
)


def serialize_aws_json_1_1(value: AIRecommendationMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AIRecommendationMetric value: {data!r}")
    return cast(AIRecommendationMetric, data)
