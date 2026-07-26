"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentActionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.version


class GetAgentActionGroupRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the action group belongs to.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent that the action group belongs to.</p>"""
    action_group_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group for which to get information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentActionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentActionGroupRequest:
    out: GetAgentActionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
