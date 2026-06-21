"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonPropagateTags``."""

from typing import Literal, TypeAlias, cast

DaemonPropagateTags: TypeAlias = Literal[
    "DAEMON",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonPropagateTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonPropagateTags:
    return cast(DaemonPropagateTags, data)
