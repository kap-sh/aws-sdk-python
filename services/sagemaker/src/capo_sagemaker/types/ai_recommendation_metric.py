"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationMetric``."""

from typing import Literal, TypeAlias, cast

AIRecommendationMetric: TypeAlias = Literal[
    "ttft-ms",
    "throughput",
    "cost",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIRecommendationMetric:
    return cast(AIRecommendationMetric, data)
