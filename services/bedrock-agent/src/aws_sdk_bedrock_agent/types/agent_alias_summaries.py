"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_summary

AgentAliasSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_alias_summary.AgentAliasSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasSummaries) -> list:
    import aws_sdk_bedrock_agent.types.agent_alias_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.agent_alias_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentAliasSummaries:
    import aws_sdk_bedrock_agent.types.agent_alias_summary

    out: AgentAliasSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_alias_summary.deserialize_json(item)
        )
    return out
