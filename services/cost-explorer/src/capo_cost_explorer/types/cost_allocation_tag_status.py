"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagStatus``."""

from typing import Literal, TypeAlias, cast

CostAllocationTagStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagStatus:
    return cast(CostAllocationTagStatus, data)
