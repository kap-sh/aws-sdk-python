"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UserPreferenceOverrideConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input


class UserPreferenceOverrideConfigurationInput(TypedDict, closed=True):
    extraction: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.UserPreferenceOverrideExtractionConfigurationInput"
    ]
    """<p>The extraction configuration for a user preference override.</p>"""
    consolidation: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.UserPreferenceOverrideConsolidationConfigurationInput"
    ]
    """<p>The consolidation configuration for a user preference override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPreferenceOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.serialize_json(
                value["consolidation"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserPreferenceOverrideConfigurationInput:
    out: UserPreferenceOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.deserialize_json(
                data["extraction"]
            )
        )
    if "consolidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.deserialize_json(
                data["consolidation"]
            )
        )
    return out
