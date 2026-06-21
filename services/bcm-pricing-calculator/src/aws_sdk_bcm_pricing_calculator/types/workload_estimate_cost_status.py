"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateCostStatus``."""

from typing import Literal, TypeAlias, cast

WorkloadEstimateCostStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "STALE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateCostStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateCostStatus:
    return cast(WorkloadEstimateCostStatus, data)
