"""Generated from Smithy shape ``com.amazonaws.apigateway#GetGatewayResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.gateway_response_type
    import capo_api_gateway.types.string


class GetGatewayResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType"
    """<p>The response type of the associated GatewayResponse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayResponseRequest:
    out: GetGatewayResponseRequest = {}  # type: ignore[typeddict-item]
    return out
