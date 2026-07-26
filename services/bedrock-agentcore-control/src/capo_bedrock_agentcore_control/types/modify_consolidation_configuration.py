"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyConsolidationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input


class _ModifyConsolidationConfiguration_customConsolidationConfiguration(
    TypedDict, closed=True
):
    customConsolidationConfiguration: "capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.CustomConsolidationConfigurationInput"


ModifyConsolidationConfiguration: TypeAlias = (
    _ModifyConsolidationConfiguration_customConsolidationConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyConsolidationConfiguration) -> dict:
    if "customConsolidationConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.serialize_json(
                value["customConsolidationConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyConsolidationConfiguration:
    if "customConsolidationConfiguration" in data:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.deserialize_json(
                data["customConsolidationConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ModifyConsolidationConfiguration: no recognized variant key"
        )
