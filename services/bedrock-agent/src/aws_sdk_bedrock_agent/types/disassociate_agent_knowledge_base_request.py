"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DisassociateAgentKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.id


class DisassociateAgentKnowledgeBaseRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent from which to disassociate the knowledge base.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent from which to disassociate the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAgentKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAgentKnowledgeBaseRequest:
    out: DisassociateAgentKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out
