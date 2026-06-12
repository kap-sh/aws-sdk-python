"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentKnowledgeBaseSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_knowledge_base_summary

AgentKnowledgeBaseSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_knowledge_base_summary.AgentKnowledgeBaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentKnowledgeBaseSummaries) -> list:
    import aws_sdk_bedrock_agent.types.agent_knowledge_base_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.agent_knowledge_base_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentKnowledgeBaseSummaries:
    import aws_sdk_bedrock_agent.types.agent_knowledge_base_summary

    out: AgentKnowledgeBaseSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_knowledge_base_summary.deserialize_json(
                item
            )
        )
    return out
