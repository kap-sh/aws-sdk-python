"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateWirelessGatewayFromThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class DisassociateWirelessGatewayFromThingRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateWirelessGatewayFromThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateWirelessGatewayFromThingRequest:
    out: DisassociateWirelessGatewayFromThingRequest = {}  # type: ignore[typeddict-item]
    return out
