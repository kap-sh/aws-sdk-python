"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoutingRuleAction``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.routing_rule_action

__listOfRoutingRuleAction: TypeAlias = list[
    "aws_sdk_apigatewayv2.types.routing_rule_action.RoutingRuleAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingRuleAction) -> list:
    import aws_sdk_apigatewayv2.types.routing_rule_action

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.routing_rule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoutingRuleAction:
    import aws_sdk_apigatewayv2.types.routing_rule_action

    out: __listOfRoutingRuleAction = []
    for item in data:
        out.append(
            aws_sdk_apigatewayv2.types.routing_rule_action.deserialize_json(item)
        )
    return out
