"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetIntegrationResponseRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    integration_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""
    integration_response_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The integration response ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationResponseRequest:
    out: GetIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    return out
