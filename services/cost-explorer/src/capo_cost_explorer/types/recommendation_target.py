"""Generated from Smithy shape ``com.amazonaws.costexplorer#RecommendationTarget``."""

from typing import Literal, TypeAlias, cast

RecommendationTarget: TypeAlias = Literal[
    "SAME_INSTANCE_FAMILY",
    "CROSS_INSTANCE_FAMILY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationTarget) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationTarget:
    return cast(RecommendationTarget, data)
