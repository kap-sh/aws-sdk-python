"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "AVAILABLE",
    "FAILED",
    "DELETED",
    "MAINTENANCE",
    "UPDATING_INSTANCE_TYPE",
    "REBOOTING",
    "REBOOT_FAILED",
    "PARTIALLY_AVAILABLE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
