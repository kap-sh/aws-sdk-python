"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_arn
    import aws_sdk_iot_wireless.types.wireless_device_id


class CreateWirelessDeviceResponse(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.wireless_device_arn.WirelessDeviceArn"]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the new wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessDeviceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWirelessDeviceResponse:
    out: CreateWirelessDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
