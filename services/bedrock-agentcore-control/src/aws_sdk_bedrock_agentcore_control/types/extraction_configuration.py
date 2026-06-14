"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration


class _ExtractionConfiguration_customExtractionConfiguration(TypedDict):
    customExtractionConfiguration: "aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration.CustomExtractionConfiguration"


ExtractionConfiguration: TypeAlias = (
    _ExtractionConfiguration_customExtractionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfiguration) -> dict:
    if "customExtractionConfiguration" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration

        return {
            "customExtractionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration.serialize_json(
                value["customExtractionConfiguration"]
            )
        }
    else:
        raise SerializationError("ExtractionConfiguration: no variant present")


def deserialize_json(data: dict) -> ExtractionConfiguration:
    if "customExtractionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration

        return {
            "customExtractionConfiguration": aws_sdk_bedrock_agentcore_control.types.custom_extraction_configuration.deserialize_json(
                data["customExtractionConfiguration"]
            )
        }
    else:
        raise DeserializationError("ExtractionConfiguration: no recognized variant key")
