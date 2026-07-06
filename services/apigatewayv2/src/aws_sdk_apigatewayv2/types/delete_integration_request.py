"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteIntegrationRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    integration_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationRequest:
    out: DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
