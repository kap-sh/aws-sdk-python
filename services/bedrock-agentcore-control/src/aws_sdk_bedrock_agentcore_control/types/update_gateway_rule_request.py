"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.actions
    import aws_sdk_bedrock_agentcore_control.types.conditions
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_priority


class UpdateGatewayRuleRequest(TypedDict, closed=True):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway containing the rule.</p>"""
    rule_id: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the rule to update.</p>"""
    priority: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
    ]
    """<p>The updated priority of the rule.</p>"""
    conditions: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.conditions.Conditions"
    ]
    """<p>The updated conditions for the rule.</p>"""
    actions: NotRequired["aws_sdk_bedrock_agentcore_control.types.actions.Actions"]
    """<p>The updated actions for the rule.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
    ]
    """<p>The updated description of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRuleRequest) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "conditions" in value:
        import aws_sdk_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            aws_sdk_bedrock_agentcore_control.types.conditions.serialize_json(
                value["conditions"]
            )
        )
    if "actions" in value:
        import aws_sdk_bedrock_agentcore_control.types.actions

        out["actions"] = aws_sdk_bedrock_agentcore_control.types.actions.serialize_json(
            value["actions"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayRuleRequest:
    out: UpdateGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "conditions" in data:
        import aws_sdk_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            aws_sdk_bedrock_agentcore_control.types.conditions.deserialize_json(
                data["conditions"]
            )
        )
    if "actions" in data:
        import aws_sdk_bedrock_agentcore_control.types.actions

        out["actions"] = (
            aws_sdk_bedrock_agentcore_control.types.actions.deserialize_json(
                data["actions"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
