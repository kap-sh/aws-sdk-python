"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ReflectionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration
    import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration


class _ReflectionConfiguration_customReflectionConfiguration(TypedDict):
    customReflectionConfiguration: "aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration.CustomReflectionConfiguration"


class _ReflectionConfiguration_episodicReflectionConfiguration(TypedDict):
    episodicReflectionConfiguration: "aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration.EpisodicReflectionConfiguration"


ReflectionConfiguration: TypeAlias = (
    _ReflectionConfiguration_customReflectionConfiguration
    | _ReflectionConfiguration_episodicReflectionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ReflectionConfiguration) -> dict:
    if "customReflectionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration

        return {
            "customReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration.serialize_json(
                value["customReflectionConfiguration"]
            )
        }
    elif "episodicReflectionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration

        return {
            "episodicReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration.serialize_json(
                value["episodicReflectionConfiguration"]
            )
        }
    else:
        raise SerializationError("ReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> ReflectionConfiguration:
    if "customReflectionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration

        return {
            "customReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_reflection_configuration.deserialize_json(
                data["customReflectionConfiguration"]
            )
        }
    elif "episodicReflectionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration

        return {
            "episodicReflectionConfiguration": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_configuration.deserialize_json(
                data["episodicReflectionConfiguration"]
            )
        }
    else:
        raise DeserializationError("ReflectionConfiguration: no recognized variant key")
