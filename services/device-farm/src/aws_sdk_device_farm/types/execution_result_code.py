"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionResultCode``."""

from typing import Literal, TypeAlias, cast

ExecutionResultCode: TypeAlias = Literal[
    "PARSING_FAILED",
    "VPC_ENDPOINT_SETUP_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionResultCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionResultCode:
    return cast(ExecutionResultCode, data)
