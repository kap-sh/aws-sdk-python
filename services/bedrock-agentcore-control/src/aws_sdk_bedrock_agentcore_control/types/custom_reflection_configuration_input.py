"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomReflectionConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input


class _CustomReflectionConfigurationInput_episodicReflectionOverride(TypedDict):
    episodicReflectionOverride: "aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.EpisodicOverrideReflectionConfigurationInput"


CustomReflectionConfigurationInput: TypeAlias = (
    _CustomReflectionConfigurationInput_episodicReflectionOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomReflectionConfigurationInput) -> dict:
    if "episodicReflectionOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        return {
            "episodicReflectionOverride": aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.serialize_json(
                value["episodicReflectionOverride"]
            )
        }
    else:
        raise SerializationError(
            "CustomReflectionConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> CustomReflectionConfigurationInput:
    if "episodicReflectionOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        return {
            "episodicReflectionOverride": aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.deserialize_json(
                data["episodicReflectionOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomReflectionConfigurationInput: no recognized variant key"
        )
