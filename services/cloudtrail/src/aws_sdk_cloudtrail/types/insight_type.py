"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightType``."""

from typing import Literal, TypeAlias, cast

InsightType: TypeAlias = Literal[
    "ApiCallRateInsight",
    "ApiErrorRateInsight",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightType:
    return cast(InsightType, data)
