"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteGatewayResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.gateway_response_type
    import aws_sdk_api_gateway.types.string


class DeleteGatewayResponseRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    response_type: "aws_sdk_api_gateway.types.gateway_response_type.GatewayResponseType"
    """<p>The response type of the associated GatewayResponse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayResponseRequest:
    out: DeleteGatewayResponseRequest = {}  # type: ignore[typeddict-item]
    return out
