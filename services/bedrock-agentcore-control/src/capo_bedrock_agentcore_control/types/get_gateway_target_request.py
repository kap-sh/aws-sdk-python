"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.target_id


class GetGatewayTargetRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway that contains the target.</p>"""
    target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the target to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayTargetRequest:
    out: GetGatewayTargetRequest = {}  # type: ignore[typeddict-item]
    return out
