"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoSnapshotStatus``."""

from typing import Literal, TypeAlias, cast

AutoSnapshotStatus: TypeAlias = Literal[
    "Success",
    "Failed",
    "InProgress",
    "NotFound",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoSnapshotStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoSnapshotStatus:
    return cast(AutoSnapshotStatus, data)
