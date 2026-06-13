"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CollaboratorConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.collaborator_configuration

CollaboratorConfigurations: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.collaborator_configuration.CollaboratorConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaboratorConfigurations) -> list:
    import aws_sdk_bedrock_agent_runtime.types.collaborator_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.collaborator_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaboratorConfigurations:
    import aws_sdk_bedrock_agent_runtime.types.collaborator_configuration

    out: CollaboratorConfigurations = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.collaborator_configuration.deserialize_json(
                item
            )
        )
    return out
