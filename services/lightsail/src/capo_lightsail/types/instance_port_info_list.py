"""Generated from Smithy shape ``com.amazonaws.lightsail#InstancePortInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.instance_port_info

InstancePortInfoList: TypeAlias = list[
    "capo_lightsail.types.instance_port_info.InstancePortInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePortInfoList) -> list:
    import capo_lightsail.types.instance_port_info

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.instance_port_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePortInfoList:
    import capo_lightsail.types.instance_port_info

    out: InstancePortInfoList = []
    for item in data:
        out.append(
            capo_lightsail.types.instance_port_info.deserialize_aws_json_1_1(item)
        )
    return out
