"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyStrategyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration
    import aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration
    import aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration
    import aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration


class ModifyStrategyConfiguration(TypedDict):
    extraction: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration.ModifyExtractionConfiguration"
    ]
    """<p>The updated extraction configuration.</p>"""
    consolidation: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration.ModifyConsolidationConfiguration"
    ]
    """<p>The updated consolidation configuration.</p>"""
    reflection: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration.ModifyReflectionConfiguration"
    ]
    """<p>The updated reflection configuration.</p>"""
    self_managed_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration.ModifySelfManagedConfiguration"
    ]
    """<p>The updated self-managed configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyStrategyConfiguration) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration.serialize_json(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration

        out["reflection"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration.serialize_json(
                value["reflection"]
            )
        )
    if "self_managed_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration

        out["selfManagedConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration.serialize_json(
                value["self_managed_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModifyStrategyConfiguration:
    out: ModifyStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_extraction_configuration.deserialize_json(
                data["extraction"]
            )
        )
    if "consolidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_consolidation_configuration.deserialize_json(
                data["consolidation"]
            )
        )
    if "reflection" in data:
        import aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration

        out["reflection"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_reflection_configuration.deserialize_json(
                data["reflection"]
            )
        )
    if "selfManagedConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration

        out["self_managed_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_self_managed_configuration.deserialize_json(
                data["selfManagedConfiguration"]
            )
        )
    return out
