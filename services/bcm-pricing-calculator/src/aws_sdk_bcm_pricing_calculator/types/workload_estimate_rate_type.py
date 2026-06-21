"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateRateType``."""

from typing import Literal, TypeAlias, cast

WorkloadEstimateRateType: TypeAlias = Literal[
    "BEFORE_DISCOUNTS",
    "AFTER_DISCOUNTS",
    "AFTER_DISCOUNTS_AND_COMMITMENTS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateRateType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateRateType:
    return cast(WorkloadEstimateRateType, data)
