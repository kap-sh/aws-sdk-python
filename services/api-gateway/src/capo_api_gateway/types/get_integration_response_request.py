"""Generated from Smithy shape ``com.amazonaws.apigateway#GetIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class GetIntegrationResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>Specifies a get integration response request's resource identifier.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>Specifies a get integration response request's HTTP method.</p>"""
    status_code: "capo_api_gateway.types.status_code.StatusCode"
    """<p>Specifies a get integration response request's status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationResponseRequest:
    out: GetIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    return out
