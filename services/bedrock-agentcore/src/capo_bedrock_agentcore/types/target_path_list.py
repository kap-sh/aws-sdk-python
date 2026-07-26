"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TargetPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.path_pattern

TargetPathList: TypeAlias = list[
    "capo_bedrock_agentcore.types.path_pattern.PathPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetPathList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetPathList:
    return list(data)
