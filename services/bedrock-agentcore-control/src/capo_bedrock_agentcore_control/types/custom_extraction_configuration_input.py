"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomExtractionConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input
    import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input


class _CustomExtractionConfigurationInput_semanticExtractionOverride(
    TypedDict, closed=True
):
    semanticExtractionOverride: "capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.SemanticOverrideExtractionConfigurationInput"


class _CustomExtractionConfigurationInput_userPreferenceExtractionOverride(
    TypedDict, closed=True
):
    userPreferenceExtractionOverride: "capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.UserPreferenceOverrideExtractionConfigurationInput"


class _CustomExtractionConfigurationInput_episodicExtractionOverride(
    TypedDict, closed=True
):
    episodicExtractionOverride: "capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.EpisodicOverrideExtractionConfigurationInput"


CustomExtractionConfigurationInput: TypeAlias = (
    _CustomExtractionConfigurationInput_semanticExtractionOverride
    | _CustomExtractionConfigurationInput_userPreferenceExtractionOverride
    | _CustomExtractionConfigurationInput_episodicExtractionOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomExtractionConfigurationInput) -> dict:
    if "semanticExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.serialize_json(
                value["semanticExtractionOverride"]
            )
        }
    elif "userPreferenceExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.serialize_json(
                value["userPreferenceExtractionOverride"]
            )
        }
    elif "episodicExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.serialize_json(
                value["episodicExtractionOverride"]
            )
        }
    else:
        raise SerializationError(
            "CustomExtractionConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> CustomExtractionConfigurationInput:
    if "semanticExtractionOverride" in data:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.deserialize_json(
                data["semanticExtractionOverride"]
            )
        }
    elif "userPreferenceExtractionOverride" in data:
        import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.deserialize_json(
                data["userPreferenceExtractionOverride"]
            )
        }
    elif "episodicExtractionOverride" in data:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.deserialize_json(
                data["episodicExtractionOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomExtractionConfigurationInput: no recognized variant key"
        )
