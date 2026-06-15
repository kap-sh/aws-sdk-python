"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetTrafficSplitEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry

TargetTrafficSplitEntries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry.TargetTrafficSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetTrafficSplitEntries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TargetTrafficSplitEntries:
    import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry

    out: TargetTrafficSplitEntries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entry.deserialize_json(
                item
            )
        )
    return out
