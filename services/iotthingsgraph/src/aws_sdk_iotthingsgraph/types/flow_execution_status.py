"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

FlowExecutionStatus: TypeAlias = Literal[
    "RUNNING",
    "ABORTED",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowExecutionStatus:
    return cast(FlowExecutionStatus, data)
