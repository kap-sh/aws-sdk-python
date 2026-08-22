"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_knowledge_base


class UpdateAgentKnowledgeBaseResponse(TypedDict, closed=True):
    agent_knowledge_base: (
        "capo_bedrock_agent.types.agent_knowledge_base.AgentKnowledgeBase"
    )
    """<p>Contains details about the knowledge base that has been associated with an agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_knowledge_base

    out["agentKnowledgeBase"] = (
        capo_bedrock_agent.types.agent_knowledge_base.serialize_json(
            value["agent_knowledge_base"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentKnowledgeBaseResponse:
    out: UpdateAgentKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentKnowledgeBase") is not None:
        import capo_bedrock_agent.types.agent_knowledge_base

        out["agent_knowledge_base"] = (
            capo_bedrock_agent.types.agent_knowledge_base.deserialize_json(
                data["agentKnowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentKnowledgeBaseResponse.agent_knowledge_base required"
        )
    return out
