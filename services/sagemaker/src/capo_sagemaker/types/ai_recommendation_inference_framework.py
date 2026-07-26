"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInferenceFramework``."""

from typing import Literal, TypeAlias, cast

AIRecommendationInferenceFramework: TypeAlias = Literal[
    "LMI",
    "VLLM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationInferenceFramework) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationInferenceFramework:
    return cast(AIRecommendationInferenceFramework, data)
