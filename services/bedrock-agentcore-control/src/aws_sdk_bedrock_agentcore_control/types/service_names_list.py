"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServiceNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.service_name

ServiceNamesList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.service_name.ServiceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceNamesList:
    return list(data)
