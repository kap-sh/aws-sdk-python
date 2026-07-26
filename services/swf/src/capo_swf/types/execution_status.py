"""Generated from Smithy shape ``com.amazonaws.swf#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
