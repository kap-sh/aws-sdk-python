"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionStatusReason``."""

from typing import Literal, TypeAlias, cast

ExecutionStatusReason: TypeAlias = Literal[
    "INSUFFICIENT_PERMISSION",
    "BILL_OWNER_CHANGED",
    "INTERNAL_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatusReason:
    return cast(ExecutionStatusReason, data)
