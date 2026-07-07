"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteRouteRequestParameterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteRouteRequestParameterRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    request_parameter_key: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route request parameter key.</p>"""
    route_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteRequestParameterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouteRequestParameterRequest:
    out: DeleteRouteRequestParameterRequest = {}  # type: ignore[typeddict-item]
    return out
