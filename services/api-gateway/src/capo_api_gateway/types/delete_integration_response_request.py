"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class DeleteIntegrationResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>Specifies a delete integration response request's resource identifier.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>Specifies a delete integration response request's HTTP method.</p>"""
    status_code: "capo_api_gateway.types.status_code.StatusCode"
    """<p>Specifies a delete integration response request's status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationResponseRequest:
    out: DeleteIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    return out
