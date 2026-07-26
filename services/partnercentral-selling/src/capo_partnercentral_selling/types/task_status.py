"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
