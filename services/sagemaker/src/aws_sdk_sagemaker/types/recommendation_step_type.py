"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationStepType``."""

from typing import Literal, TypeAlias, cast

RecommendationStepType: TypeAlias = Literal["BENCHMARK",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationStepType:
    return cast(RecommendationStepType, data)
