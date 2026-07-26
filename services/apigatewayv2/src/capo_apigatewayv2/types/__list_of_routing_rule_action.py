"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoutingRuleAction``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.routing_rule_action

__listOfRoutingRuleAction: TypeAlias = list[
    "capo_apigatewayv2.types.routing_rule_action.RoutingRuleAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingRuleAction) -> list:
    import capo_apigatewayv2.types.routing_rule_action

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.routing_rule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoutingRuleAction:
    import capo_apigatewayv2.types.routing_rule_action

    out: __listOfRoutingRuleAction = []
    for item in data:
        out.append(capo_apigatewayv2.types.routing_rule_action.deserialize_json(item))
    return out
