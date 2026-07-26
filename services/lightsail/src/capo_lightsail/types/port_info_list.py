"""Generated from Smithy shape ``com.amazonaws.lightsail#PortInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.port_info

PortInfoList: TypeAlias = list["capo_lightsail.types.port_info.PortInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortInfoList) -> list:
    import capo_lightsail.types.port_info

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.port_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PortInfoList:
    import capo_lightsail.types.port_info

    out: PortInfoList = []
    for item in data:
        out.append(capo_lightsail.types.port_info.deserialize_aws_json_1_1(item))
    return out
