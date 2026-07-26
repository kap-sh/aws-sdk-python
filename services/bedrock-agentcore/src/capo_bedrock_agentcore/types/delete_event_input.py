"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.event_id
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.session_id


class DeleteEventInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource from which to delete the event.</p>"""
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The identifier of the session containing the event to delete.</p>"""
    event_id: "capo_bedrock_agentcore.types.event_id.EventId"
    """<p>The identifier of the event to delete.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with the event to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventInput:
    out: DeleteEventInput = {}  # type: ignore[typeddict-item]
    return out
