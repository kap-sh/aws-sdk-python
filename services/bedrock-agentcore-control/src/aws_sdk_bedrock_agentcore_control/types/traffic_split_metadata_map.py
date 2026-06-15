"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_key
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_value

TrafficSplitMetadataMap: TypeAlias = dict[
    "aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_key.TrafficSplitMetadataKey",
    "aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_value.TrafficSplitMetadataValue",
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
        out[key] = value
    return out
