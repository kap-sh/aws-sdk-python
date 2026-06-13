"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

class _CustomConsolidationConfigurationInput_semanticConsolidationOverride(TypedDict):
    semanticConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.SemanticOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_summaryConsolidationOverride(TypedDict):
    summaryConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.SummaryOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_userPreferenceConsolidationOverride(TypedDict):
    userPreferenceConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.UserPreferenceOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_episodicConsolidationOverride(TypedDict):
    episodicConsolidationOverride: "aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.EpisodicOverrideConsolidationConfigurationInput"

CustomConsolidationConfigurationInput: TypeAlias = _CustomConsolidationConfigurationInput_semanticConsolidationOverride | _CustomConsolidationConfigurationInput_summaryConsolidationOverride | _CustomConsolidationConfigurationInput_userPreferenceConsolidationOverride | _CustomConsolidationConfigurationInput_episodicConsolidationOverride

# --- restJson1 ser/de ---
def serialize_json(value: CustomConsolidationConfigurationInput) -> dict:
    if "semanticConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
        return {"semanticConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.serialize_json(value["semanticConsolidationOverride"])}
    elif "summaryConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input
        return {"summaryConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.serialize_json(value["summaryConsolidationOverride"])}
    elif "userPreferenceConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input
        return {"userPreferenceConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.serialize_json(value["userPreferenceConsolidationOverride"])}
    elif "episodicConsolidationOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
        return {"episodicConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.serialize_json(value["episodicConsolidationOverride"])}
    else:
        raise SerializationError("CustomConsolidationConfigurationInput: no variant present")


def deserialize_json(data: dict) -> CustomConsolidationConfigurationInput:
    if "semanticConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
        return {"semanticConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.deserialize_json(data["semanticConsolidationOverride"])}
    elif "summaryConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input
        return {"summaryConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.deserialize_json(data["summaryConsolidationOverride"])}
    elif "userPreferenceConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input
        return {"userPreferenceConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.deserialize_json(data["userPreferenceConsolidationOverride"])}
    elif "episodicConsolidationOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
        return {"episodicConsolidationOverride": aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.deserialize_json(data["episodicConsolidationOverride"])}
    else:
        raise DeserializationError("CustomConsolidationConfigurationInput: no recognized variant key")