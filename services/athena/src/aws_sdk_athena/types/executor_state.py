"""Generated from Smithy shape ``com.amazonaws.athena#ExecutorState``."""

from typing import Literal, TypeAlias, cast

ExecutorState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "REGISTERED",
    "TERMINATING",
    "TERMINATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutorState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutorState:
    return cast(ExecutorState, data)
