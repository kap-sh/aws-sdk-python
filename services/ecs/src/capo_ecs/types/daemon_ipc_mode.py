"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonIpcMode``."""

from typing import Literal, TypeAlias, cast

DaemonIpcMode: TypeAlias = Literal[
    "none",
    "shared",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonIpcMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonIpcMode:
    return cast(DaemonIpcMode, data)
