"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_summary

TargetSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummaries) -> list:
    import capo_bedrock_agentcore_control.types.target_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.target_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetSummaries:
    import capo_bedrock_agentcore_control.types.target_summary

    out: TargetSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.target_summary.deserialize_json(item)
        )
    return out
