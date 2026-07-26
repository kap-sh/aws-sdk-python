"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionStatusCode``."""

from typing import Literal, TypeAlias, cast

ExecutionStatusCode: TypeAlias = Literal[
    "INITIATION_IN_PROCESS",
    "QUERY_QUEUED",
    "QUERY_IN_PROCESS",
    "QUERY_FAILURE",
    "DELIVERY_IN_PROCESS",
    "DELIVERY_SUCCESS",
    "DELIVERY_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatusCode:
    return cast(ExecutionStatusCode, data)
