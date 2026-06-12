"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaboratorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_collaborator_summary

AgentCollaboratorSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_collaborator_summary.AgentCollaboratorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorSummaries) -> list:
    import aws_sdk_bedrock_agent.types.agent_collaborator_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.agent_collaborator_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentCollaboratorSummaries:
    import aws_sdk_bedrock_agent.types.agent_collaborator_summary

    out: AgentCollaboratorSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_collaborator_summary.deserialize_json(
                item
            )
        )
    return out
