"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SemanticOverrideConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input


class SemanticOverrideConfigurationInput(TypedDict):
    extraction: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.SemanticOverrideExtractionConfigurationInput"
    ]
    """<p>The extraction configuration for a semantic override.</p>"""
    consolidation: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.SemanticOverrideConsolidationConfigurationInput"
    ]
    """<p>The consolidation configuration for a semantic override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.serialize_json(
                value["consolidation"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticOverrideConfigurationInput:
    out: SemanticOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.deserialize_json(
                data["extraction"]
            )
        )
    if "consolidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.deserialize_json(
                data["consolidation"]
            )
        )
    return out
