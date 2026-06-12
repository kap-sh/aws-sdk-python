"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_summary

AgentSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_summary.AgentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummaries) -> list:
    import aws_sdk_bedrock_agent.types.agent_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.agent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSummaries:
    import aws_sdk_bedrock_agent.types.agent_summary

    out: AgentSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.agent_summary.deserialize_json(item))
    return out
