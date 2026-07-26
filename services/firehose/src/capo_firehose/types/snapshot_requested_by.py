"""Generated from Smithy shape ``com.amazonaws.firehose#SnapshotRequestedBy``."""

from typing import Literal, TypeAlias, cast

SnapshotRequestedBy: TypeAlias = Literal[
    "USER",
    "FIREHOSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotRequestedBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotRequestedBy:
    return cast(SnapshotRequestedBy, data)
