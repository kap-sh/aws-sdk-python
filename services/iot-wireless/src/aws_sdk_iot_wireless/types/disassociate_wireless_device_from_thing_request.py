"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateWirelessDeviceFromThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_id


class DisassociateWirelessDeviceFromThingRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the resource to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWirelessDeviceFromThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWirelessDeviceFromThingRequest:
    out: DisassociateWirelessDeviceFromThingRequest = {}  # type: ignore[typeddict-item]
    return out
