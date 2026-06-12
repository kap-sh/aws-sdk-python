"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationOptimizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AIRecommendationOptimizationType: TypeAlias = Literal[
    "SpeculativeDecoding",
    "KernelTuning",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SpeculativeDecoding",
        "KernelTuning",
    )
)


def serialize_aws_json_1_1(value: AIRecommendationOptimizationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationOptimizationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AIRecommendationOptimizationType value: {data!r}"
        )
    return cast(AIRecommendationOptimizationType, data)
