"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.gateway_rule_id


class DeleteGatewayRuleRequest(TypedDict):
    gateway_identifier: (
        "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway containing the rule.</p>"""
    rule_id: "aws_sdk_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId"
    """<p>The unique identifier of the rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRuleRequest:
    out: DeleteGatewayRuleRequest = {}  # type: ignore[typeddict-item]
    return out
