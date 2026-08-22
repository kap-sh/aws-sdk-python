"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.policy_generation_summary

PolicyGenerationSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.policy_generation_summary.PolicyGenerationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.policy_generation_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.policy_generation_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PolicyGenerationSummaryList:
    import capo_bedrock_agentcore_control.types.policy_generation_summary

    out: PolicyGenerationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.policy_generation_summary.deserialize_json(
                item
            )
        )
    return out
