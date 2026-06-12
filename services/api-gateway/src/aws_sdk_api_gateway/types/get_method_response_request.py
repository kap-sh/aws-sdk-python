"""Generated from Smithy shape ``com.amazonaws.apigateway#GetMethodResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.status_code
    import aws_sdk_api_gateway.types.string


class GetMethodResponseRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Resource identifier for the MethodResponse resource.</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>The HTTP verb of the Method resource.</p>"""
    status_code: "aws_sdk_api_gateway.types.status_code.StatusCode"
    """<p>The status code for the MethodResponse resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMethodResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMethodResponseRequest:
    out: GetMethodResponseRequest = {}  # type: ignore[typeddict-item]
    return out
