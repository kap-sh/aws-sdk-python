"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskSnapshotState``."""

from typing import Literal, TypeAlias, cast

DiskSnapshotState: TypeAlias = Literal[
    "pending",
    "completed",
    "error",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskSnapshotState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskSnapshotState:
    return cast(DiskSnapshotState, data)
