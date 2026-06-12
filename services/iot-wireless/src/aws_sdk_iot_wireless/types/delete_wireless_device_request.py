"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_id


class DeleteWirelessDeviceRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessDeviceRequest:
    out: DeleteWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
