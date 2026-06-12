"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_id
    import aws_sdk_bedrock_agent.types.id


class DeleteAgentAliasRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the alias belongs to.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentAliasRequest:
    out: DeleteAgentAliasRequest = {}  # type: ignore[typeddict-item]
    return out
