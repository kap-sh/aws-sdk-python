"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.wireless_gateway_id_type


class GetWirelessGatewayRequest(TypedDict, closed=True):
    identifier: "capo_iot_wireless.types.identifier.Identifier"
    """<p>The identifier of the wireless gateway to get.</p>"""
    identifier_type: (
        "capo_iot_wireless.types.wireless_gateway_id_type.WirelessGatewayIdType"
    )
    """<p>The type of identifier used in <code>identifier</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayRequest:
    out: GetWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
