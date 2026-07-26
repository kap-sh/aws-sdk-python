"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetServiceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_service_type


class GetServiceEndpointRequest(TypedDict, closed=True):
    service_type: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_service_type.WirelessGatewayServiceType"
    ]
    """<p>The service type for which to get endpoint information about. Can be <code>CUPS</code> for the Configuration and Update Server endpoint, or <code>LNS</code> for the LoRaWAN Network Server endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceEndpointRequest:
    out: GetServiceEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
