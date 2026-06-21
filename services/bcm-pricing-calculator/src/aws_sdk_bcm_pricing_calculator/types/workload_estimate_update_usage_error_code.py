"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUpdateUsageErrorCode``."""

from typing import Literal, TypeAlias, cast

WorkloadEstimateUpdateUsageErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "NOT_FOUND",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUpdateUsageErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateUpdateUsageErrorCode:
    return cast(WorkloadEstimateUpdateUsageErrorCode, data)
