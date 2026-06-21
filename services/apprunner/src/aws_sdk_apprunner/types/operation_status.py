"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationStatus``."""

from typing import Literal, TypeAlias, cast

OperationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_FAILED",
    "ROLLBACK_SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
