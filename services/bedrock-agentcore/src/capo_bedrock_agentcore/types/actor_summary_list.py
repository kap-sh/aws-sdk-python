"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ActorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_summary

ActorSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.actor_summary.ActorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActorSummaryList) -> list:
    import capo_bedrock_agentcore.types.actor_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.actor_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorSummaryList:
    import capo_bedrock_agentcore.types.actor_summary

    out: ActorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.actor_summary.deserialize_json(item))
    return out
