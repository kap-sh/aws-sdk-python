"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.target_summary

TargetSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.target_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.target_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetSummaries:
    import aws_sdk_bedrock_agentcore_control.types.target_summary

    out: TargetSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.target_summary.deserialize_json(
                item
            )
        )
    return out
