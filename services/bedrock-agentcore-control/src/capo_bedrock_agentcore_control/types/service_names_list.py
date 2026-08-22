"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServiceNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.service_name

ServiceNamesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.service_name.ServiceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceNamesList:
    return [item for item in data if item is not None]
