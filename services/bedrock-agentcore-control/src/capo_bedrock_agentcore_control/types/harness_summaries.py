"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_summary

HarnessSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_summary.HarnessSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSummaries) -> list:
    import capo_bedrock_agentcore_control.types.harness_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessSummaries:
    import capo_bedrock_agentcore_control.types.harness_summary

    out: HarnessSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_summary.deserialize_json(item)
        )
    return out
