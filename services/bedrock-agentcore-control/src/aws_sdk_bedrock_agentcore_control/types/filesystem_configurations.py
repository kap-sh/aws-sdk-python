"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilesystemConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configuration

FilesystemConfigurations: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.filesystem_configuration.FilesystemConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: FilesystemConfigurations) -> list:
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.filesystem_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilesystemConfigurations:
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configuration
    out: FilesystemConfigurations = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.filesystem_configuration.deserialize_json(item))
    return out