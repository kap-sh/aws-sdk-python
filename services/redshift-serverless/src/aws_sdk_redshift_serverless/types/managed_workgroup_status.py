"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ManagedWorkgroupStatus``."""

from typing import Literal, TypeAlias, cast

ManagedWorkgroupStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "MODIFYING",
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedWorkgroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedWorkgroupStatus:
    return cast(ManagedWorkgroupStatus, data)
