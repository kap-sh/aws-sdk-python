"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetAuthorizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetAuthorizerRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    authorizer_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The authorizer identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAuthorizerRequest:
    out: GetAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
