"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_alias_summary

FlowAliasSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.flow_alias_summary.FlowAliasSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasSummaries) -> list:
    import aws_sdk_bedrock_agent.types.flow_alias_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_alias_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowAliasSummaries:
    import aws_sdk_bedrock_agent.types.flow_alias_summary

    out: FlowAliasSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.flow_alias_summary.deserialize_json(item)
        )
    return out
