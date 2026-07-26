"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_id

TargetIdList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.target_id.TargetId"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetIdList:
    return list(data)
