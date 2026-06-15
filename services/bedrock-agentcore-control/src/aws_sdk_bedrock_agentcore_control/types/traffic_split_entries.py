"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_entry

TrafficSplitEntries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.traffic_split_entry.TrafficSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitEntries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.traffic_split_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrafficSplitEntries:
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_entry

    out: TrafficSplitEntries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.traffic_split_entry.deserialize_json(
                item
            )
        )
    return out
