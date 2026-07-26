"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_id


class DeleteWirelessGatewayRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessGatewayRequest:
    out: DeleteWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
