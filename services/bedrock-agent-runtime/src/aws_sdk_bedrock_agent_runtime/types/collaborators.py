"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Collaborators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.collaborator

Collaborators: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.collaborator.Collaborator"
]


# --- restJson1 ser/de ---
def serialize_json(value: Collaborators) -> list:
    import aws_sdk_bedrock_agent_runtime.types.collaborator

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.collaborator.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Collaborators:
    import aws_sdk_bedrock_agent_runtime.types.collaborator

    out: Collaborators = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.collaborator.deserialize_json(item)
        )
    return out
