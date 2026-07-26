"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourcesListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.resource_type

ResourcesListType: TypeAlias = list[
    "capo_bedrock_agentcore.types.resource_type.ResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesListType) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourcesListType:
    return list(data)
