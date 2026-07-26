"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.target_id


class DeleteGatewayTargetRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway associated with the target.</p>"""
    target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the gateway target to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayTargetRequest:
    out: DeleteGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    return out
