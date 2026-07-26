"""Generated from Smithy shape ``com.amazonaws.storagegateway#ActiveDirectoryStatus``."""

from typing import Literal, TypeAlias, cast

ActiveDirectoryStatus: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DETACHED",
    "JOINED",
    "JOINING",
    "NETWORK_ERROR",
    "TIMEOUT",
    "UNKNOWN_ERROR",
    "INSUFFICIENT_PERMISSIONS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveDirectoryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveDirectoryStatus:
    return cast(ActiveDirectoryStatus, data)
