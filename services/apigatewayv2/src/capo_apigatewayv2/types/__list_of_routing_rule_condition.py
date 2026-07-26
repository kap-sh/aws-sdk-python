"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoutingRuleCondition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.routing_rule_condition

__listOfRoutingRuleCondition: TypeAlias = list[
    "capo_apigatewayv2.types.routing_rule_condition.RoutingRuleCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingRuleCondition) -> list:
    import capo_apigatewayv2.types.routing_rule_condition

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.routing_rule_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoutingRuleCondition:
    import capo_apigatewayv2.types.routing_rule_condition

    out: __listOfRoutingRuleCondition = []
    for item in data:
        out.append(
            capo_apigatewayv2.types.routing_rule_condition.deserialize_json(item)
        )
    return out
