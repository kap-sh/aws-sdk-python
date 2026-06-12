"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance

InstanceList: TypeAlias = list["aws_sdk_lightsail.types.instance.Instance"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceList) -> list:
    import aws_sdk_lightsail.types.instance

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceList:
    import aws_sdk_lightsail.types.instance

    out: InstanceList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.instance.deserialize_aws_json_1_1(item))
    return out
