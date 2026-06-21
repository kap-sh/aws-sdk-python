"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

ExecutionMode: TypeAlias = Literal[
    "Auto",
    "Interactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionMode:
    return cast(ExecutionMode, data)
