"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyExtractionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input


class _ModifyExtractionConfiguration_customExtractionConfiguration(TypedDict):
    customExtractionConfiguration: "aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input.CustomExtractionConfigurationInput"


ModifyExtractionConfiguration: TypeAlias = (
    _ModifyExtractionConfiguration_customExtractionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyExtractionConfiguration) -> dict:
    if "customExtractionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input

        return {
            "customExtractionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input.serialize_json(
                value["customExtractionConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyExtractionConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyExtractionConfiguration:
    if "customExtractionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input

        return {
            "customExtractionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration_input.deserialize_json(
                data["customExtractionConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ModifyExtractionConfiguration: no recognized variant key"
        )
