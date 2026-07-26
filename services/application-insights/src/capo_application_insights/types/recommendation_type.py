"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RecommendationType``."""

from typing import Literal, TypeAlias, cast

RecommendationType: TypeAlias = Literal[
    "INFRA_ONLY",
    "WORKLOAD_ONLY",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
