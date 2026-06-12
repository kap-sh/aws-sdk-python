"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_version_summary

FlowVersionSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.flow_version_summary.FlowVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowVersionSummaries) -> list:
    import aws_sdk_bedrock_agent.types.flow_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.flow_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowVersionSummaries:
    import aws_sdk_bedrock_agent.types.flow_version_summary

    out: FlowVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.flow_version_summary.deserialize_json(item)
        )
    return out
