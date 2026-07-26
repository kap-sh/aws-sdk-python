"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotFilterName``."""

from typing import Literal, TypeAlias, cast

SnapshotFilterName: TypeAlias = Literal[
    "file-system-id",
    "volume-id",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotFilterName:
    return cast(SnapshotFilterName, data)
