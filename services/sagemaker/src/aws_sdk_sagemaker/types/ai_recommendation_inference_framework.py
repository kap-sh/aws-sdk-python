"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInferenceFramework``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AIRecommendationInferenceFramework: TypeAlias = Literal[
    "LMI",
    "VLLM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LMI",
        "VLLM",
    )
)


def serialize_aws_json_1_1(value: AIRecommendationInferenceFramework) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationInferenceFramework:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AIRecommendationInferenceFramework value: {data!r}"
        )
    return cast(AIRecommendationInferenceFramework, data)
