"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AssociateAgentKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_knowledge_base


class AssociateAgentKnowledgeBaseResponse(TypedDict):
    agent_knowledge_base: (
        "aws_sdk_bedrock_agent.types.agent_knowledge_base.AgentKnowledgeBase"
    )
    """<p>Contains details about the knowledge base that has been associated with the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAgentKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_knowledge_base

    out["agentKnowledgeBase"] = (
        aws_sdk_bedrock_agent.types.agent_knowledge_base.serialize_json(
            value["agent_knowledge_base"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateAgentKnowledgeBaseResponse:
    out: AssociateAgentKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "agentKnowledgeBase" in data:
        import aws_sdk_bedrock_agent.types.agent_knowledge_base

        out["agent_knowledge_base"] = (
            aws_sdk_bedrock_agent.types.agent_knowledge_base.deserialize_json(
                data["agentKnowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateAgentKnowledgeBaseResponse.agent_knowledge_base required"
        )
    return out
