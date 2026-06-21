"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonStatus``."""

from typing import Literal, TypeAlias, cast

DaemonStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonStatus:
    return cast(DaemonStatus, data)
