"""Generated from Smithy shape ``com.amazonaws.odb#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "FAILED",
    "PROVISIONING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
    "MAINTENANCE_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
