"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateStatus``."""

from typing import Literal, TypeAlias, cast

BillEstimateStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillEstimateStatus:
    return cast(BillEstimateStatus, data)
