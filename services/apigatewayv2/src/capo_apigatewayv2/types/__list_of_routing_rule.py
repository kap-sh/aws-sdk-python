"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoutingRule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.routing_rule

__listOfRoutingRule: TypeAlias = list[
    "capo_apigatewayv2.types.routing_rule.RoutingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingRule) -> list:
    import capo_apigatewayv2.types.routing_rule

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.routing_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoutingRule:
    import capo_apigatewayv2.types.routing_rule

    out: __listOfRoutingRule = []
    for item in data:
        out.append(capo_apigatewayv2.types.routing_rule.deserialize_json(item))
    return out
