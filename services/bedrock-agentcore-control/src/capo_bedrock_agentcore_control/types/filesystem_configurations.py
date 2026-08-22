"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilesystemConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.filesystem_configuration

FilesystemConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.filesystem_configuration.FilesystemConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilesystemConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.filesystem_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.filesystem_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FilesystemConfigurations:
    import capo_bedrock_agentcore_control.types.filesystem_configuration

    out: FilesystemConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.filesystem_configuration.deserialize_json(
                item
            )
        )
    return out
