"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.actions
    import aws_sdk_bedrock_agentcore_control.types.conditions
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.gateway_arn
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_priority
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status
    import aws_sdk_bedrock_agentcore_control.types.system_managed_block


class CreateGatewayRuleResponse(TypedDict, closed=True):
    rule_id: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the gateway rule.</p>"""
    gateway_arn: "aws_sdk_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway that the rule belongs to.</p>"""
    priority: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
    """<p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.</p>"""
    conditions: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.conditions.Conditions"
    ]
    """<p>The conditions that must be met for the rule to apply.</p>"""
    actions: "aws_sdk_bedrock_agentcore_control.types.actions.Actions"
    """<p>The actions to take when the rule conditions are met.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
    ]
    """<p>The description of the gateway rule.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the rule was created.</p>"""
    status: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.GatewayRuleStatus"
    )
    """<p>The current status of the rule.</p>"""
    system: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.system_managed_block.SystemManagedBlock"
    ]
    """<p>System-managed metadata for rules created by automated processes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["gatewayArn"] = value["gateway_arn"]
    out["priority"] = value["priority"]
    if "conditions" in value:
        import aws_sdk_bedrock_agentcore_control.types.conditions

        out["conditions"] = (
            aws_sdk_bedrock_agentcore_control.types.conditions.serialize_json(
                value["conditions"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.actions

    out["actions"] = aws_sdk_bedrock_agentcore_control.types.actions.serialize_json(
        value["actions"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.serialize_json(
            value["status"]
        )
    )
    if "system" in value:
        import aws_sdk_bedrock_agentcore_control.types.system_managed_block

        out["system"] = (
            aws_sdk_bedrock_agentcore_control.types.system_managed_block.serialize_json(
                value["system"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayRuleResponse:
    out: CreateGatewayRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.rule_id required")
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.gateway_arn required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateGatewayRuleResponse.priority required")
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
    else:
        raise DeserializationError("CreateGatewayRuleResponse.actions required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRuleResponse.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRuleResponse.status required")
    if "system" in data:
        import aws_sdk_bedrock_agentcore_control.types.system_managed_block

        out["system"] = (
            aws_sdk_bedrock_agentcore_control.types.system_managed_block.deserialize_json(
                data["system"]
            )
        )
    return out
