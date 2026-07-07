"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteAuthorizerRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    authorizer_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the Authorizer resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAuthorizerRequest:
    out: DeleteAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
