"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.routing_rule_priority


class CreateRoutingRuleRequest(TypedDict, closed=True):
    actions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
    ]
    """<p>Represents a routing rule action. The only supported action is invokeApi.</p>"""
    conditions: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
    ]
    """<p>Represents a condition. Conditions can contain up to two matchHeaders conditions and one matchBasePaths conditions. API Gateway evaluates header conditions and base path conditions together. You can only use AND between header and base path conditions.</p>"""
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    priority: NotRequired[
        "aws_sdk_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
    ]
    """Represents the priority of the routing rule."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoutingRuleRequest) -> dict:
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


def deserialize_json(data: dict) -> CreateRoutingRuleRequest:
    out: CreateRoutingRuleRequest = {}  # type: ignore[typeddict-item]
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
