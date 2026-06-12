"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RouteResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.route_models
    import aws_sdk_apigatewayv2.types.route_parameters
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key


class RouteResponse(TypedDict):
    model_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>Represents the model selection expression of a route response. Supported only for WebSocket APIs.</p>"""
    response_models: NotRequired["aws_sdk_apigatewayv2.types.route_models.RouteModels"]
    """<p>Represents the response models of a route response.</p>"""
    response_parameters: NotRequired[
        "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
    ]
    """<p>Represents the response parameters of a route response.</p>"""
    route_response_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>Represents the identifier of a route response.</p>"""
    route_response_key: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
    ]
    """<p>Represents the route response key of a route response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteResponse) -> dict:
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
    if "route_response_id" in value:
        out["routeResponseId"] = value["route_response_id"]
    if "route_response_key" in value:
        out["routeResponseKey"] = value["route_response_key"]
    return out


def deserialize_json(data: dict) -> RouteResponse:
    out: RouteResponse = {}  # type: ignore[typeddict-item]
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
    if "routeResponseId" in data:
        out["route_response_id"] = data["routeResponseId"]
    if "routeResponseKey" in data:
        out["route_response_key"] = data["routeResponseKey"]
    return out
