"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_summary

FlowSummaries: TypeAlias = list["capo_bedrock_agent.types.flow_summary.FlowSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummaries) -> list:
    import capo_bedrock_agent.types.flow_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowSummaries:
    import capo_bedrock_agent.types.flow_summary

    out: FlowSummaries = []
    for item in data:
        out.append(capo_bedrock_agent.types.flow_summary.deserialize_json(item))
    return out
