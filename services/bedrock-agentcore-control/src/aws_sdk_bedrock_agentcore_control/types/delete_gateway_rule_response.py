"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status

class DeleteGatewayRuleResponse(TypedDict):
    rule_id: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the deleted rule.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.GatewayRuleStatus"
    """<p>The status of the rule deletion operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteGatewayRuleResponse:
    out: DeleteGatewayRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("DeleteGatewayRuleResponse.rule_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_rule_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.gateway_rule_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteGatewayRuleResponse.status required")
    return out