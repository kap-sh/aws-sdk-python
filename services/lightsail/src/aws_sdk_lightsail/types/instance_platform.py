"""Generated from Smithy shape ``com.amazonaws.lightsail#InstancePlatform``."""

from typing import Literal, TypeAlias, cast

InstancePlatform: TypeAlias = Literal[
    "LINUX_UNIX",
    "WINDOWS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePlatform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePlatform:
    return cast(InstancePlatform, data)
