"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeleteIntegrationResponseRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    integration_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""
    integration_response_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The integration response ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationResponseRequest:
    out: DeleteIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    return out
