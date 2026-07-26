"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConsolidationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_consolidation_override
    import capo_bedrock_agentcore_control.types.semantic_consolidation_override
    import capo_bedrock_agentcore_control.types.summary_consolidation_override
    import capo_bedrock_agentcore_control.types.user_preference_consolidation_override


class _CustomConsolidationConfiguration_semanticConsolidationOverride(
    TypedDict, closed=True
):
    semanticConsolidationOverride: "capo_bedrock_agentcore_control.types.semantic_consolidation_override.SemanticConsolidationOverride"


class _CustomConsolidationConfiguration_summaryConsolidationOverride(
    TypedDict, closed=True
):
    summaryConsolidationOverride: "capo_bedrock_agentcore_control.types.summary_consolidation_override.SummaryConsolidationOverride"


class _CustomConsolidationConfiguration_userPreferenceConsolidationOverride(
    TypedDict, closed=True
):
    userPreferenceConsolidationOverride: "capo_bedrock_agentcore_control.types.user_preference_consolidation_override.UserPreferenceConsolidationOverride"


class _CustomConsolidationConfiguration_episodicConsolidationOverride(
    TypedDict, closed=True
):
    episodicConsolidationOverride: "capo_bedrock_agentcore_control.types.episodic_consolidation_override.EpisodicConsolidationOverride"


CustomConsolidationConfiguration: TypeAlias = (
    _CustomConsolidationConfiguration_semanticConsolidationOverride
    | _CustomConsolidationConfiguration_summaryConsolidationOverride
    | _CustomConsolidationConfiguration_userPreferenceConsolidationOverride
    | _CustomConsolidationConfiguration_episodicConsolidationOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConsolidationConfiguration) -> dict:
    if "semanticConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_consolidation_override.serialize_json(
                value["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_consolidation_override.serialize_json(
                value["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_consolidation_override.serialize_json(
                value["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_consolidation_override.serialize_json(
                value["episodicConsolidationOverride"]
            )
        }
    else:
        raise SerializationError("CustomConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomConsolidationConfiguration:
    if "semanticConsolidationOverride" in data:
        import capo_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_consolidation_override.deserialize_json(
                data["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in data:
        import capo_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_consolidation_override.deserialize_json(
                data["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in data:
        import capo_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_consolidation_override.deserialize_json(
                data["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in data:
        import capo_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_consolidation_override.deserialize_json(
                data["episodicConsolidationOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomConsolidationConfiguration: no recognized variant key"
        )
