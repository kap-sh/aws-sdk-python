"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConsolidationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override
    import aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override
    import aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override
    import aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override


class _CustomConsolidationConfiguration_semanticConsolidationOverride(TypedDict):
    semanticConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override.SemanticConsolidationOverride"


class _CustomConsolidationConfiguration_summaryConsolidationOverride(TypedDict):
    summaryConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override.SummaryConsolidationOverride"


class _CustomConsolidationConfiguration_userPreferenceConsolidationOverride(TypedDict):
    userPreferenceConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override.UserPreferenceConsolidationOverride"


class _CustomConsolidationConfiguration_episodicConsolidationOverride(TypedDict):
    episodicConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override.EpisodicConsolidationOverride"


CustomConsolidationConfiguration: TypeAlias = (
    _CustomConsolidationConfiguration_semanticConsolidationOverride
    | _CustomConsolidationConfiguration_summaryConsolidationOverride
    | _CustomConsolidationConfiguration_userPreferenceConsolidationOverride
    | _CustomConsolidationConfiguration_episodicConsolidationOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConsolidationConfiguration) -> dict:
    if "semanticConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override.serialize_json(
                value["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override.serialize_json(
                value["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override.serialize_json(
                value["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override.serialize_json(
                value["episodicConsolidationOverride"]
            )
        }
    else:
        raise SerializationError("CustomConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomConsolidationConfiguration:
    if "semanticConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.semantic_consolidation_override.deserialize_json(
                data["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.summary_consolidation_override.deserialize_json(
                data["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.user_preference_consolidation_override.deserialize_json(
                data["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.episodic_consolidation_override.deserialize_json(
                data["episodicConsolidationOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomConsolidationConfiguration: no recognized variant key"
        )
