"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationStatus``."""

from typing import Literal, TypeAlias, cast

OperationStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PENDING",
    "SUCCESS",
    "FAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
