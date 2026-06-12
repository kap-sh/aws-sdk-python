"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteIntegrationResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.status_code
    import aws_sdk_api_gateway.types.string


class DeleteIntegrationResponseRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a delete integration response request's resource identifier.</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a delete integration response request's HTTP method.</p>"""
    status_code: "aws_sdk_api_gateway.types.status_code.StatusCode"
    """<p>Specifies a delete integration response request's status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationResponseRequest:
    out: DeleteIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    return out
