"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceSnapshotState``."""

from typing import Literal, TypeAlias, cast

InstanceSnapshotState: TypeAlias = Literal[
    "pending",
    "error",
    "available",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSnapshotState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceSnapshotState:
    return cast(InstanceSnapshotState, data)
