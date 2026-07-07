"""Generated from Smithy shape ``com.amazonaws.apigateway#GetAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetAuthorizerRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    authorizer_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the Authorizer resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAuthorizerRequest:
    out: GetAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
