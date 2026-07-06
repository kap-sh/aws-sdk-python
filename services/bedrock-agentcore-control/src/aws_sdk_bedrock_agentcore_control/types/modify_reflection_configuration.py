"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyReflectionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input


class _ModifyReflectionConfiguration_episodicReflectionConfiguration(
    TypedDict, closed=True
):
    episodicReflectionConfiguration: "aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input.EpisodicReflectionConfigurationInput"


class _ModifyReflectionConfiguration_customReflectionConfiguration(
    TypedDict, closed=True
):
    customReflectionConfiguration: "aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input.CustomReflectionConfigurationInput"


ModifyReflectionConfiguration: TypeAlias = (
    _ModifyReflectionConfiguration_episodicReflectionConfiguration
    | _ModifyReflectionConfiguration_customReflectionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyReflectionConfiguration) -> dict:
    if "episodicReflectionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input

        return {
            "episodicReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input.serialize_json(
                value["episodicReflectionConfiguration"]
            )
        }
    elif "customReflectionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input

        return {
            "customReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input.serialize_json(
                value["customReflectionConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyReflectionConfiguration:
    if "episodicReflectionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input

        return {
            "episodicReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration_input.deserialize_json(
                data["episodicReflectionConfiguration"]
            )
        }
    elif "customReflectionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input

        return {
            "customReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration_input.deserialize_json(
                data["customReflectionConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ModifyReflectionConfiguration: no recognized variant key"
        )
