"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomReflectionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override


class _CustomReflectionConfiguration_episodicReflectionOverride(TypedDict, closed=True):
    episodicReflectionOverride: "aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override.EpisodicReflectionOverride"


CustomReflectionConfiguration: TypeAlias = (
    _CustomReflectionConfiguration_episodicReflectionOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomReflectionConfiguration) -> dict:
    if "episodicReflectionOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override

        return {
            "episodicReflectionOverride": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override.serialize_json(
                value["episodicReflectionOverride"]
            )
        }
    else:
        raise SerializationError("CustomReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomReflectionConfiguration:
    if "episodicReflectionOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override

        return {
            "episodicReflectionOverride": aws_sdk_bedrock_agentcore_control.types.episodic_reflection_override.deserialize_json(
                data["episodicReflectionOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomReflectionConfiguration: no recognized variant key"
        )
