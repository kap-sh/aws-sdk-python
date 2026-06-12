"""Generated from Smithy shape ``com.amazonaws.lightsail#InstancePlatformList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_platform

InstancePlatformList: TypeAlias = list[
    "aws_sdk_lightsail.types.instance_platform.InstancePlatform"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePlatformList) -> list:
    import aws_sdk_lightsail.types.instance_platform

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.instance_platform.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePlatformList:
    import aws_sdk_lightsail.types.instance_platform

    out: InstancePlatformList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.instance_platform.deserialize_aws_json_1_1(item)
        )
    return out
