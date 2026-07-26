"""Generated from Smithy shape ``com.amazonaws.ecs#PidMode``."""

from typing import Literal, TypeAlias, cast

PidMode: TypeAlias = Literal[
    "host",
    "task",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PidMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PidMode:
    return cast(PidMode, data)
