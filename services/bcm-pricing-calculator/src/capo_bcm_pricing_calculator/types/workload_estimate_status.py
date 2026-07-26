"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateStatus``."""

from typing import Literal, TypeAlias, cast

WorkloadEstimateStatus: TypeAlias = Literal[
    "UPDATING",
    "VALID",
    "INVALID",
    "ACTION_NEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateStatus:
    return cast(WorkloadEstimateStatus, data)
