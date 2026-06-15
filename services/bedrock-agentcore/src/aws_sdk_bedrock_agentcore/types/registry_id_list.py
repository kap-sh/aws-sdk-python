"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RegistryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.registry_identifier

RegistryIdList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.registry_identifier.RegistryIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegistryIdList:
    return list(data)
