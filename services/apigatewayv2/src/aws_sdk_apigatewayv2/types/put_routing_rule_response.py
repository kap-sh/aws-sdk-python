"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PutRoutingRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition
    import aws_sdk_apigatewayv2.types.arn
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.routing_rule_priority


class PutRoutingRuleResponse(TypedDict):
    actions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
    ]
    """<p>The routing rule action.</p>"""
    conditions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
    ]
    """<p>The conditions of the routing rule.</p>"""
    priority: NotRequired[
        "aws_sdk_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
    ]
    """<p>The routing rule priority.</p>"""
    routing_rule_arn: NotRequired["aws_sdk_apigatewayv2.types.arn.Arn"]
    """<p>The routing rule ARN.</p>"""
    routing_rule_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The routing rule ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRoutingRuleResponse) -> dict:
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
    if "routing_rule_arn" in value:
        out["routingRuleArn"] = value["routing_rule_arn"]
    if "routing_rule_id" in value:
        out["routingRuleId"] = value["routing_rule_id"]
    return out


def deserialize_json(data: dict) -> PutRoutingRuleResponse:
    out: PutRoutingRuleResponse = {}  # type: ignore[typeddict-item]
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
    if "routingRuleArn" in data:
        out["routing_rule_arn"] = data["routingRuleArn"]
    if "routingRuleId" in data:
        out["routing_rule_id"] = data["routingRuleId"]
    return out
