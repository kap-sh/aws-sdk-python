"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateWirelessDeviceFromMulticastGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.wireless_device_id


class DisassociateWirelessDeviceFromMulticastGroupRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
    wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWirelessDeviceFromMulticastGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWirelessDeviceFromMulticastGroupRequest:
    out: DisassociateWirelessDeviceFromMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    return out
