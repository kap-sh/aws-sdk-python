"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandLogging``."""

from typing import Literal, TypeAlias, cast

ExecuteCommandLogging: TypeAlias = Literal[
    "NONE",
    "DEFAULT",
    "OVERRIDE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandLogging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecuteCommandLogging:
    return cast(ExecuteCommandLogging, data)
