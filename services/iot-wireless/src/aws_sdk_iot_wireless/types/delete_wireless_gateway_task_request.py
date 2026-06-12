"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessGatewayTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class DeleteWirelessGatewayTaskRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessGatewayTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessGatewayTaskRequest:
    out: DeleteWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
    return out
