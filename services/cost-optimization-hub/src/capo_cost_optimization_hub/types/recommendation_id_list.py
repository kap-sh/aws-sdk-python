"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RecommendationIdList``."""

from typing import TypeAlias

RecommendationIdList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RecommendationIdList:
    return list(data)
