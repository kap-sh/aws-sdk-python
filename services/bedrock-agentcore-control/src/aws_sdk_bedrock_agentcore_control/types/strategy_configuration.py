"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StrategyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.consolidation_configuration
    import aws_sdk_bedrock_agentcore_control.types.extraction_configuration
    import aws_sdk_bedrock_agentcore_control.types.override_type
    import aws_sdk_bedrock_agentcore_control.types.reflection_configuration
    import aws_sdk_bedrock_agentcore_control.types.self_managed_configuration


class StrategyConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.override_type.OverrideType"
    ]
    """<p>The type of override for the strategy configuration.</p>"""
    extraction: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.extraction_configuration.ExtractionConfiguration"
    ]
    """<p>The extraction configuration for the memory strategy.</p>"""
    consolidation: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.consolidation_configuration.ConsolidationConfiguration"
    ]
    """<p>The consolidation configuration for the memory strategy.</p>"""
    reflection: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.reflection_configuration.ReflectionConfiguration"
    ]
    """<p>The reflection configuration for the memory strategy.</p>"""
    self_managed_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.self_managed_configuration.SelfManagedConfiguration"
    ]
    """<p>Self-managed configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StrategyConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agentcore_control.types.override_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.override_type.serialize_json(
                value["type"]
            )
        )
    if "extraction" in value:
        import aws_sdk_bedrock_agentcore_control.types.extraction_configuration

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_configuration.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.consolidation_configuration

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.consolidation_configuration.serialize_json(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import aws_sdk_bedrock_agentcore_control.types.reflection_configuration

        out["reflection"] = (
            aws_sdk_bedrock_agentcore_control.types.reflection_configuration.serialize_json(
                value["reflection"]
            )
        )
    if "self_managed_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.self_managed_configuration

        out["selfManagedConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.self_managed_configuration.serialize_json(
                value["self_managed_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StrategyConfiguration:
    out: StrategyConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.override_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.override_type.deserialize_json(
                data["type"]
            )
        )
    if "extraction" in data:
        import aws_sdk_bedrock_agentcore_control.types.extraction_configuration

        out["extraction"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_configuration.deserialize_json(
                data["extraction"]
            )
        )
    if "consolidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.consolidation_configuration

        out["consolidation"] = (
            aws_sdk_bedrock_agentcore_control.types.consolidation_configuration.deserialize_json(
                data["consolidation"]
            )
        )
    if "reflection" in data:
        import aws_sdk_bedrock_agentcore_control.types.reflection_configuration

        out["reflection"] = (
            aws_sdk_bedrock_agentcore_control.types.reflection_configuration.deserialize_json(
                data["reflection"]
            )
        )
    if "selfManagedConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.self_managed_configuration

        out["self_managed_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.self_managed_configuration.deserialize_json(
                data["selfManagedConfiguration"]
            )
        )
    return out
