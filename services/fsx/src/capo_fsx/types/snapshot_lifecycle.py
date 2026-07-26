"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotLifecycle``."""

from typing import Literal, TypeAlias, cast

SnapshotLifecycle: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "DELETING",
    "AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotLifecycle:
    return cast(SnapshotLifecycle, data)
