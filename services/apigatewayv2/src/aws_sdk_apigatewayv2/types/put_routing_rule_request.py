"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PutRoutingRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.routing_rule_priority


class PutRoutingRuleRequest(TypedDict):
    actions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
    ]
    """<p>The routing rule action.</p>"""
    conditions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
    ]
    """<p>The routing rule condition.</p>"""
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    priority: NotRequired[
        "aws_sdk_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
    ]
    """<p>The routing rule priority.</p>"""
    routing_rule_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The routing rule ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRoutingRuleRequest) -> dict:
    out: dict = {}
    if "actions" in value:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action

        out["actions"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.serialize_json(
                value["actions"]
            )
        )
    if "conditions" in value:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition

        out["conditions"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.serialize_json(
                value["conditions"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> PutRoutingRuleRequest:
    out: PutRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action

        out["actions"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.deserialize_json(
                data["actions"]
            )
        )
    if "conditions" in data:
        import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition

        out["conditions"] = (
            aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.deserialize_json(
                data["conditions"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    return out
