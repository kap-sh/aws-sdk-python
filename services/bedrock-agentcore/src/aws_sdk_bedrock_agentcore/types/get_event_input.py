"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetEventInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.actor_id
    import aws_sdk_bedrock_agentcore.types.event_id
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.session_id

class GetEventInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource containing the event.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId"
    """<p>The identifier of the session containing the event.</p>"""
    actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with the event.</p>"""
    event_id: "aws_sdk_bedrock_agentcore.types.event_id.EventId"
    """<p>The identifier of the event to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventInput:
    out: GetEventInput = {}  # type: ignore[typeddict-item]
    return out