"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "MODIFYING",
    "UPDATING",
    "DELETED",
    "FAILED",
    "UPDATING_DEPLOYMENT_TYPE",
    "UPDATING_INSTANCE_TYPE",
    "MAINTENANCE",
    "REBOOTING",
    "REBOOT_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Status) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Status:
    return cast(Status, data)
