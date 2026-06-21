"""Generated from Smithy shape ``com.amazonaws.datasync#TaskMode``."""

from typing import Literal, TypeAlias, cast

TaskMode: TypeAlias = Literal[
    "BASIC",
    "ENHANCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskMode:
    return cast(TaskMode, data)
