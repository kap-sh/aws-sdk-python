"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class GetWirelessGatewayTaskRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayTaskRequest:
    out: GetWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
    return out
