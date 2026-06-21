"""Generated from Smithy shape ``com.amazonaws.firehose#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "SUSPENDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotStatus:
    return cast(SnapshotStatus, data)
