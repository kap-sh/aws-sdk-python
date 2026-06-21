"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoMountStatus``."""

from typing import Literal, TypeAlias, cast

AutoMountStatus: TypeAlias = Literal[
    "Failed",
    "Pending",
    "Mounted",
    "NotMounted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMountStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMountStatus:
    return cast(AutoMountStatus, data)
