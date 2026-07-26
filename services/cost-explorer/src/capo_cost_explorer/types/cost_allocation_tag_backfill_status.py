"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagBackfillStatus``."""

from typing import Literal, TypeAlias, cast

CostAllocationTagBackfillStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagBackfillStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagBackfillStatus:
    return cast(CostAllocationTagBackfillStatus, data)
