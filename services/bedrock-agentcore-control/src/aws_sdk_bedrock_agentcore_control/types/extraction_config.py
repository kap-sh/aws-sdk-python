"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.llm_extraction_config


class _ExtractionConfig_llmExtractionConfig(TypedDict):
    llmExtractionConfig: "aws_sdk_bedrock_agentcore_control.types.llm_extraction_config.LlmExtractionConfig"


ExtractionConfig: TypeAlias = _ExtractionConfig_llmExtractionConfig


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfig) -> dict:
    if "llmExtractionConfig" in value:
        import aws_sdk_bedrock_agentcore_control.types.llm_extraction_config

        return {
            "llmExtractionConfig": aws_sdk_bedrock_agentcore_control.types.llm_extraction_config.serialize_json(
                value["llmExtractionConfig"]
            )
        }
    else:
        raise SerializationError("ExtractionConfig: no variant present")


def deserialize_json(data: dict) -> ExtractionConfig:
    if "llmExtractionConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.llm_extraction_config

        return {
            "llmExtractionConfig": aws_sdk_bedrock_agentcore_control.types.llm_extraction_config.deserialize_json(
                data["llmExtractionConfig"]
            )
        }
    else:
        raise DeserializationError("ExtractionConfig: no recognized variant key")
