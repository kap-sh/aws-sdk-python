"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayFirmwareInformationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class GetWirelessGatewayFirmwareInformationRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayFirmwareInformationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayFirmwareInformationRequest:
    out: GetWirelessGatewayFirmwareInformationRequest = {}  # type: ignore[typeddict-item]
    return out
