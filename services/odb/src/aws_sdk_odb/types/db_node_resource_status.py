"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeResourceStatus``."""

from typing import Literal, TypeAlias, cast

DbNodeResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "FAILED",
    "PROVISIONING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "STARTING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbNodeResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbNodeResourceStatus:
    return cast(DbNodeResourceStatus, data)
