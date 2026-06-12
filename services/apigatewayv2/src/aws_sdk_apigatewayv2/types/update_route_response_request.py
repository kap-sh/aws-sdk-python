"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateRouteResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.route_models
    import aws_sdk_apigatewayv2.types.route_parameters
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key


class UpdateRouteResponseRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    model_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The model selection expression for the route response. Supported only for WebSocket APIs.</p>"""
    response_models: NotRequired["aws_sdk_apigatewayv2.types.route_models.RouteModels"]
    """<p>The response models for the route response.</p>"""
    response_parameters: NotRequired[
        "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
    ]
    """<p>The route response parameters.</p>"""
    route_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""
    route_response_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route response ID.</p>"""
    route_response_key: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
    ]
    """<p>The route response key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteResponseRequest) -> dict:
    out: dict = {}
    if "model_selection_expression" in value:
        out["modelSelectionExpression"] = value["model_selection_expression"]
    if "response_models" in value:
        import aws_sdk_apigatewayv2.types.route_models

        out["responseModels"] = aws_sdk_apigatewayv2.types.route_models.serialize_json(
            value["response_models"]
        )
    if "response_parameters" in value:
        import aws_sdk_apigatewayv2.types.route_parameters

        out["responseParameters"] = (
            aws_sdk_apigatewayv2.types.route_parameters.serialize_json(
                value["response_parameters"]
            )
        )
    if "route_response_key" in value:
        out["routeResponseKey"] = value["route_response_key"]
    return out


def deserialize_json(data: dict) -> UpdateRouteResponseRequest:
    out: UpdateRouteResponseRequest = {}  # type: ignore[typeddict-item]
    if "modelSelectionExpression" in data:
        out["model_selection_expression"] = data["modelSelectionExpression"]
    if "responseModels" in data:
        import aws_sdk_apigatewayv2.types.route_models

        out["response_models"] = (
            aws_sdk_apigatewayv2.types.route_models.deserialize_json(
                data["responseModels"]
            )
        )
    if "responseParameters" in data:
        import aws_sdk_apigatewayv2.types.route_parameters

        out["response_parameters"] = (
            aws_sdk_apigatewayv2.types.route_parameters.deserialize_json(
                data["responseParameters"]
            )
        )
    if "routeResponseKey" in data:
        out["route_response_key"] = data["routeResponseKey"]
    return out
