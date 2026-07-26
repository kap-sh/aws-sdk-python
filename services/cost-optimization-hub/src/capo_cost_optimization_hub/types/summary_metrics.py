"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SummaryMetrics``."""

from typing import Literal, TypeAlias, cast

SummaryMetrics: TypeAlias = Literal["SavingsPercentage",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SummaryMetrics:
    return cast(SummaryMetrics, data)
