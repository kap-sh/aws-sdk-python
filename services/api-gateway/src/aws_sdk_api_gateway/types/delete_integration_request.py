"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteIntegrationRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a delete integration request's resource identifier.</p>"""
    http_method: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a delete integration request's HTTP method.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationRequest:
    out: DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
