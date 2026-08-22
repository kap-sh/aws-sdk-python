"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.traffic_split_entry

TrafficSplitEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.traffic_split_entry.TrafficSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitEntries) -> list:
    import capo_bedrock_agentcore_control.types.traffic_split_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.traffic_split_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrafficSplitEntries:
    import capo_bedrock_agentcore_control.types.traffic_split_entry

    out: TrafficSplitEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.traffic_split_entry.deserialize_json(
                item
            )
        )
    return out
