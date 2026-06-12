"""Generated from Smithy shape ``com.amazonaws.apigateway#GetIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetIntegrationRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a get integration request's resource identifier</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a get integration request's HTTP method.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationRequest:
    out: GetIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
