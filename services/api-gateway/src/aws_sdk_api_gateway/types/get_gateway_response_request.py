"""Generated from Smithy shape ``com.amazonaws.apigateway#GetGatewayResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.gateway_response_type
    import aws_sdk_api_gateway.types.string


class GetGatewayResponseRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    response_type: "aws_sdk_api_gateway.types.gateway_response_type.GatewayResponseType"
    """<p>The response type of the associated GatewayResponse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayResponseRequest:
    out: GetGatewayResponseRequest = {}  # type: ignore[typeddict-item]
    return out
