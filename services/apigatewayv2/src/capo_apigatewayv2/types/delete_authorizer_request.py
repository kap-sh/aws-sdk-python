"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeleteAuthorizerRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    authorizer_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The authorizer identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAuthorizerRequest:
    out: DeleteAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
