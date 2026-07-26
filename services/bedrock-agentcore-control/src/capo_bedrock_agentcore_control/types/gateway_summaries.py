"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewaySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_summary

GatewaySummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_summary.GatewaySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewaySummaries) -> list:
    import capo_bedrock_agentcore_control.types.gateway_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GatewaySummaries:
    import capo_bedrock_agentcore_control.types.gateway_summary

    out: GatewaySummaries = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_summary.deserialize_json(item)
        )
    return out
