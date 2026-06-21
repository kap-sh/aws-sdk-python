"""Generated from Smithy shape ``com.amazonaws.ecs#IpcMode``."""

from typing import Literal, TypeAlias, cast

IpcMode: TypeAlias = Literal[
    "host",
    "task",
    "none",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpcMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpcMode:
    return cast(IpcMode, data)
