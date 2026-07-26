"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "Running",
    "InvalidQuery",
    "Complete",
    "Failed",
    "Timeout",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
