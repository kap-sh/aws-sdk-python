"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAllocationStatus``."""

from typing import Literal, TypeAlias, cast

CapacityAllocationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAllocationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityAllocationStatus:
    return cast(CapacityAllocationStatus, data)
