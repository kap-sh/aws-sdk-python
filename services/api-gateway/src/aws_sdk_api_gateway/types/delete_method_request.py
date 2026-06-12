"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteMethodRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteMethodRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Resource identifier for the Method resource.</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>The HTTP verb of the Method resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMethodRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMethodRequest:
    out: DeleteMethodRequest = {}  # type: ignore[typeddict-item]
    return out
