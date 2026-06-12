"""Generated from Smithy shape ``com.amazonaws.iotwireless#NetworkAnalyzerMulticastGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id

NetworkAnalyzerMulticastGroupList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAnalyzerMulticastGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkAnalyzerMulticastGroupList:
    return list(data)
