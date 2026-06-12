"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetIntegrationRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    integration_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationRequest:
    out: GetIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
