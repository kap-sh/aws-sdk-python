"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteMethodResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class DeleteMethodResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>The Resource identifier for the MethodResponse resource.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>The HTTP verb of the Method resource.</p>"""
    status_code: "capo_api_gateway.types.status_code.StatusCode"
    """<p>The status code identifier for the MethodResponse resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMethodResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMethodResponseRequest:
    out: DeleteMethodResponseRequest = {}  # type: ignore[typeddict-item]
    return out
