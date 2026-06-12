"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_version_summary

AgentVersionSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_version_summary.AgentVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentVersionSummaries) -> list:
    import aws_sdk_bedrock_agent.types.agent_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.agent_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentVersionSummaries:
    import aws_sdk_bedrock_agent.types.agent_version_summary

    out: AgentVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_version_summary.deserialize_json(item)
        )
    return out
