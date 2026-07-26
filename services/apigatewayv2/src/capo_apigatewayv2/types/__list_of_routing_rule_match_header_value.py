"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoutingRuleMatchHeaderValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.routing_rule_match_header_value

__listOfRoutingRuleMatchHeaderValue: TypeAlias = list[
    "capo_apigatewayv2.types.routing_rule_match_header_value.RoutingRuleMatchHeaderValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingRuleMatchHeaderValue) -> list:
    import capo_apigatewayv2.types.routing_rule_match_header_value

    out: list = []
    for item in value:
        out.append(
            capo_apigatewayv2.types.routing_rule_match_header_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfRoutingRuleMatchHeaderValue:
    import capo_apigatewayv2.types.routing_rule_match_header_value

    out: __listOfRoutingRuleMatchHeaderValue = []
    for item in data:
        out.append(
            capo_apigatewayv2.types.routing_rule_match_header_value.deserialize_json(
                item
            )
        )
    return out
