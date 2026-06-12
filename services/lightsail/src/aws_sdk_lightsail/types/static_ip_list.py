"""Generated from Smithy shape ``com.amazonaws.lightsail#StaticIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.static_ip

StaticIpList: TypeAlias = list["aws_sdk_lightsail.types.static_ip.StaticIp"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StaticIpList) -> list:
    import aws_sdk_lightsail.types.static_ip

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.static_ip.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StaticIpList:
    import aws_sdk_lightsail.types.static_ip

    out: StaticIpList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.static_ip.deserialize_aws_json_1_1(item))
    return out
