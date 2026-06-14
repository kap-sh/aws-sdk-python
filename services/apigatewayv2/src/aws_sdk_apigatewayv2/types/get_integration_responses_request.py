"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetIntegrationResponsesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetIntegrationResponsesRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    integration_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""
    max_results: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationResponsesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationResponsesRequest:
    out: GetIntegrationResponsesRequest = {}  # type: ignore[typeddict-item]
    return out
