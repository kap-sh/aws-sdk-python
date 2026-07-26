"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationOptimizationType``."""

from typing import Literal, TypeAlias, cast

AIRecommendationOptimizationType: TypeAlias = Literal[
    "SpeculativeDecoding",
    "KernelTuning",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationOptimizationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationOptimizationType:
    return cast(AIRecommendationOptimizationType, data)
