"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeregisterWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.wireless_device_type


class DeregisterWirelessDeviceRequest(TypedDict, closed=True):
    identifier: "capo_iot_wireless.types.identifier.Identifier"
    """<p>The identifier of the wireless device to deregister from AWS IoT Wireless.</p>"""
    wireless_device_type: NotRequired[
        "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The type of wireless device to deregister from AWS IoT Wireless, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterWirelessDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterWirelessDeviceRequest:
    out: DeregisterWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
