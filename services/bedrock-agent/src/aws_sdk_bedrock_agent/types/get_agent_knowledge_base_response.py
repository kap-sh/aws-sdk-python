"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_knowledge_base


class GetAgentKnowledgeBaseResponse(TypedDict, closed=True):
    agent_knowledge_base: (
        "aws_sdk_bedrock_agent.types.agent_knowledge_base.AgentKnowledgeBase"
    )
    """<p>Contains details about a knowledge base attached to an agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_knowledge_base

    out["agentKnowledgeBase"] = (
        aws_sdk_bedrock_agent.types.agent_knowledge_base.serialize_json(
            value["agent_knowledge_base"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAgentKnowledgeBaseResponse:
    out: GetAgentKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "agentKnowledgeBase" in data:
        import aws_sdk_bedrock_agent.types.agent_knowledge_base

        out["agent_knowledge_base"] = (
            aws_sdk_bedrock_agent.types.agent_knowledge_base.deserialize_json(
                data["agentKnowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentKnowledgeBaseResponse.agent_knowledge_base required"
        )
    return out
