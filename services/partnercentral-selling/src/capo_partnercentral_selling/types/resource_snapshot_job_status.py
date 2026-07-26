"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotJobStatus``."""

from typing import Literal, TypeAlias, cast

ResourceSnapshotJobStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceSnapshotJobStatus:
    return cast(ResourceSnapshotJobStatus, data)
