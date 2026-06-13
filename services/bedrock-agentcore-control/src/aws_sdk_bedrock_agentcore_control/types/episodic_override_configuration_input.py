"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EpisodicOverrideConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

class EpisodicOverrideConfigurationInput(TypedDict):
    extraction: NotRequired["aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.EpisodicOverrideExtractionConfigurationInput"]
    """<p>Contains configurations for overriding the extraction step of the episodic memory strategy.</p>"""
    consolidation: NotRequired["aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.EpisodicOverrideConsolidationConfigurationInput"]
    """<p>Contains configurations for overriding the consolidation step of the episodic memory strategy.</p>"""
    reflection: NotRequired["aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.EpisodicOverrideReflectionConfigurationInput"]
    """<p>Contains configurations for overriding the reflection step of the episodic memory strategy.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EpisodicOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
        out["extraction"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.serialize_json(value["extraction"])
    if "consolidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
        out["consolidation"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.serialize_json(value["consolidation"])
    if "reflection" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input
        out["reflection"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.serialize_json(value["reflection"])
    return out


def deserialize_json(data: dict) -> EpisodicOverrideConfigurationInput:
    out: EpisodicOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
        out["extraction"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.deserialize_json(data["extraction"])
    if "consolidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
        out["consolidation"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.deserialize_json(data["consolidation"])
    if "reflection" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input
        out["reflection"] = aws_sdk_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.deserialize_json(data["reflection"])
    return out