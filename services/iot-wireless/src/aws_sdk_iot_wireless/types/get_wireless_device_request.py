"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.identifier
    import aws_sdk_iot_wireless.types.wireless_device_id_type


class GetWirelessDeviceRequest(TypedDict):
    identifier: "aws_sdk_iot_wireless.types.identifier.Identifier"
    """<p>The identifier of the wireless device to get.</p>"""
    identifier_type: (
        "aws_sdk_iot_wireless.types.wireless_device_id_type.WirelessDeviceIdType"
    )
    """<p>The type of identifier used in <code>identifier</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceRequest:
    out: GetWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
