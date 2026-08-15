"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonPidMode``."""

from typing import Literal, TypeAlias, cast

DaemonPidMode: TypeAlias = Literal[
    "none",
    "shared",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonPidMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonPidMode:
    return cast(DaemonPidMode, data)
