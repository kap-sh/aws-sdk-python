"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightsMetricDataType``."""

from typing import Literal, TypeAlias, cast

InsightsMetricDataType: TypeAlias = Literal[
    "FillWithZeros",
    "NonZeroData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightsMetricDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightsMetricDataType:
    return cast(InsightsMetricDataType, data)
