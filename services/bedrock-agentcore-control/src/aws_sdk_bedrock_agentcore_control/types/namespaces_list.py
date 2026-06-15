"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NamespacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.namespace

NamespacesList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.namespace.Namespace"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespacesList) -> list:
    return list(value)


def deserialize_json(data: list) -> NamespacesList:
    return list(data)
