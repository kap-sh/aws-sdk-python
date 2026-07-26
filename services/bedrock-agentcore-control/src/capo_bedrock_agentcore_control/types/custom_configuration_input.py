"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_configuration_input
    import capo_bedrock_agentcore_control.types.self_managed_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_configuration_input
    import capo_bedrock_agentcore_control.types.summary_override_configuration_input
    import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input


class _CustomConfigurationInput_semanticOverride(TypedDict, closed=True):
    semanticOverride: "capo_bedrock_agentcore_control.types.semantic_override_configuration_input.SemanticOverrideConfigurationInput"


class _CustomConfigurationInput_summaryOverride(TypedDict, closed=True):
    summaryOverride: "capo_bedrock_agentcore_control.types.summary_override_configuration_input.SummaryOverrideConfigurationInput"


class _CustomConfigurationInput_userPreferenceOverride(TypedDict, closed=True):
    userPreferenceOverride: "capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.UserPreferenceOverrideConfigurationInput"


class _CustomConfigurationInput_episodicOverride(TypedDict, closed=True):
    episodicOverride: "capo_bedrock_agentcore_control.types.episodic_override_configuration_input.EpisodicOverrideConfigurationInput"


class _CustomConfigurationInput_selfManagedConfiguration(TypedDict, closed=True):
    selfManagedConfiguration: "capo_bedrock_agentcore_control.types.self_managed_configuration_input.SelfManagedConfigurationInput"


CustomConfigurationInput: TypeAlias = (
    _CustomConfigurationInput_semanticOverride
    | _CustomConfigurationInput_summaryOverride
    | _CustomConfigurationInput_userPreferenceOverride
    | _CustomConfigurationInput_episodicOverride
    | _CustomConfigurationInput_selfManagedConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConfigurationInput) -> dict:
    if "semanticOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_configuration_input

        return {
            "semanticOverride": capo_bedrock_agentcore_control.types.semantic_override_configuration_input.serialize_json(
                value["semanticOverride"]
            )
        }
    elif "summaryOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_override_configuration_input

        return {
            "summaryOverride": capo_bedrock_agentcore_control.types.summary_override_configuration_input.serialize_json(
                value["summaryOverride"]
            )
        }
    elif "userPreferenceOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input

        return {
            "userPreferenceOverride": capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.serialize_json(
                value["userPreferenceOverride"]
            )
        }
    elif "episodicOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_configuration_input

        return {
            "episodicOverride": capo_bedrock_agentcore_control.types.episodic_override_configuration_input.serialize_json(
                value["episodicOverride"]
            )
        }
    elif "selfManagedConfiguration" in value:
        import capo_bedrock_agentcore_control.types.self_managed_configuration_input

        return {
            "selfManagedConfiguration": capo_bedrock_agentcore_control.types.self_managed_configuration_input.serialize_json(
                value["selfManagedConfiguration"]
            )
        }
    else:
        raise SerializationError("CustomConfigurationInput: no variant present")


def deserialize_json(data: dict) -> CustomConfigurationInput:
    if "semanticOverride" in data:
        import capo_bedrock_agentcore_control.types.semantic_override_configuration_input

        return {
            "semanticOverride": capo_bedrock_agentcore_control.types.semantic_override_configuration_input.deserialize_json(
                data["semanticOverride"]
            )
        }
    elif "summaryOverride" in data:
        import capo_bedrock_agentcore_control.types.summary_override_configuration_input

        return {
            "summaryOverride": capo_bedrock_agentcore_control.types.summary_override_configuration_input.deserialize_json(
                data["summaryOverride"]
            )
        }
    elif "userPreferenceOverride" in data:
        import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input

        return {
            "userPreferenceOverride": capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.deserialize_json(
                data["userPreferenceOverride"]
            )
        }
    elif "episodicOverride" in data:
        import capo_bedrock_agentcore_control.types.episodic_override_configuration_input

        return {
            "episodicOverride": capo_bedrock_agentcore_control.types.episodic_override_configuration_input.deserialize_json(
                data["episodicOverride"]
            )
        }
    elif "selfManagedConfiguration" in data:
        import capo_bedrock_agentcore_control.types.self_managed_configuration_input

        return {
            "selfManagedConfiguration": capo_bedrock_agentcore_control.types.self_managed_configuration_input.deserialize_json(
                data["selfManagedConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "CustomConfigurationInput: no recognized variant key"
        )
