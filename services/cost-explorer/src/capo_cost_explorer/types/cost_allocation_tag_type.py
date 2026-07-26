"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagType``."""

from typing import Literal, TypeAlias, cast

CostAllocationTagType: TypeAlias = Literal[
    "AWSGenerated",
    "UserDefined",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagType:
    return cast(CostAllocationTagType, data)
