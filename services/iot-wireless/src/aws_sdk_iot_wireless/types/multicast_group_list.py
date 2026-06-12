"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group

MulticastGroupList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.multicast_group.MulticastGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastGroupList) -> list:
    import aws_sdk_iot_wireless.types.multicast_group

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.multicast_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MulticastGroupList:
    import aws_sdk_iot_wireless.types.multicast_group

    out: MulticastGroupList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.multicast_group.deserialize_json(item))
    return out
