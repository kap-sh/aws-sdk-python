"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.target_id

class DeleteGatewayTargetRequest(TypedDict):
    gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    """<p>The unique identifier of the gateway associated with the target.</p>"""
    target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the gateway target to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayTargetRequest:
    out: DeleteGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    return out