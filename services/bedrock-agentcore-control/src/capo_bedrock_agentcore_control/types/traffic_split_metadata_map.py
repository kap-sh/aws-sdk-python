"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.traffic_split_metadata_key
    import capo_bedrock_agentcore_control.types.traffic_split_metadata_value

TrafficSplitMetadataMap: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.traffic_split_metadata_key.TrafficSplitMetadataKey",
    "capo_bedrock_agentcore_control.types.traffic_split_metadata_value.TrafficSplitMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TrafficSplitMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TrafficSplitMetadataMap:
    out: TrafficSplitMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
