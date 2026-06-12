"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_summary

FlowSummaries: TypeAlias = list["aws_sdk_bedrock_agent.types.flow_summary.FlowSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummaries) -> list:
    import aws_sdk_bedrock_agent.types.flow_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowSummaries:
    import aws_sdk_bedrock_agent.types.flow_summary

    out: FlowSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.flow_summary.deserialize_json(item))
    return out
