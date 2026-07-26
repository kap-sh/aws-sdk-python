"""Generated from Smithy shape ``com.amazonaws.datapipeline#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "FINISHED",
    "FAILED",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
