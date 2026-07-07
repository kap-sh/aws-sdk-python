"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.version


class GetAgentKnowledgeBaseRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent with which the knowledge base is associated.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The version of the agent with which the knowledge base is associated.</p>"""
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base associated with the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentKnowledgeBaseRequest:
    out: GetAgentKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out
