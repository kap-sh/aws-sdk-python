"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotStatus: TypeAlias = Literal[
    "CREATING",
    "READY",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    return cast(SnapshotStatus, data)
