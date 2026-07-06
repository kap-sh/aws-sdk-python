"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_gateway_arn


class CreateWirelessGatewayResponse(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_arn.WirelessGatewayArn"
    ]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the new wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayResponse:
    out: CreateWirelessGatewayResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
