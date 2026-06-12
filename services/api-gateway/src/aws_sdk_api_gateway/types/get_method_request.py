"""Generated from Smithy shape ``com.amazonaws.apigateway#GetMethodRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetMethodRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Resource identifier for the Method resource.</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies the method request's HTTP method type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMethodRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMethodRequest:
    out: GetMethodRequest = {}  # type: ignore[typeddict-item]
    return out
