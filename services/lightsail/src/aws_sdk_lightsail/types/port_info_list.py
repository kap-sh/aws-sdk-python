"""Generated from Smithy shape ``com.amazonaws.lightsail#PortInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.port_info

PortInfoList: TypeAlias = list["aws_sdk_lightsail.types.port_info.PortInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortInfoList) -> list:
    import aws_sdk_lightsail.types.port_info

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.port_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PortInfoList:
    import aws_sdk_lightsail.types.port_info

    out: PortInfoList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.port_info.deserialize_aws_json_1_1(item))
    return out
