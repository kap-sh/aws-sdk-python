"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.id


class GetAgentAliasRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent to which the alias to get information belongs.</p>"""
    agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias for which to get information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentAliasRequest:
    out: GetAgentAliasRequest = {}  # type: ignore[typeddict-item]
    return out
