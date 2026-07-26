"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PutRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of_routing_rule_action
    import capo_apigatewayv2.types.__list_of_routing_rule_condition
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.routing_rule_priority


class PutRoutingRuleRequest(TypedDict, closed=True):
    actions: NotRequired[
        "capo_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
    ]
    """<p>The routing rule action.</p>"""
    conditions: NotRequired[
        "capo_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
    ]
    """<p>The routing rule condition.</p>"""
    domain_name: "capo_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    priority: NotRequired[
        "capo_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
    ]
    """<p>The routing rule priority.</p>"""
    routing_rule_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The routing rule ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRoutingRuleRequest) -> dict:
    out: dict = {}
    if "actions" in value:
        import capo_apigatewayv2.types.__list_of_routing_rule_action

        out["actions"] = (
            capo_apigatewayv2.types.__list_of_routing_rule_action.serialize_json(
                value["actions"]
            )
        )
    if "conditions" in value:
        import capo_apigatewayv2.types.__list_of_routing_rule_condition

        out["conditions"] = (
            capo_apigatewayv2.types.__list_of_routing_rule_condition.serialize_json(
                value["conditions"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> PutRoutingRuleRequest:
    out: PutRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import capo_apigatewayv2.types.__list_of_routing_rule_action

        out["actions"] = (
            capo_apigatewayv2.types.__list_of_routing_rule_action.deserialize_json(
                data["actions"]
            )
        )
    if "conditions" in data:
        import capo_apigatewayv2.types.__list_of_routing_rule_condition

        out["conditions"] = (
            capo_apigatewayv2.types.__list_of_routing_rule_condition.deserialize_json(
                data["conditions"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    return out
