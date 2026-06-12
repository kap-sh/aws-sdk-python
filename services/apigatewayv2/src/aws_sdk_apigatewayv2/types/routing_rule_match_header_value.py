"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleMatchHeaderValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key


class RoutingRuleMatchHeaderValue(TypedDict):
    header: NotRequired["aws_sdk_apigatewayv2.types.selection_key.SelectionKey"]
    value_glob: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleMatchHeaderValue) -> dict:
    out: dict = {}
    if "header" in value:
        out["header"] = value["header"]
    if "value_glob" in value:
        out["valueGlob"] = value["value_glob"]
    return out


def deserialize_json(data: dict) -> RoutingRuleMatchHeaderValue:
    out: RoutingRuleMatchHeaderValue = {}  # type: ignore[typeddict-item]
    if "header" in data:
        out["header"] = data["header"]
    if "valueGlob" in data:
        out["value_glob"] = data["valueGlob"]
    return out
