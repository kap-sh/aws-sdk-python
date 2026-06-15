"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessModelConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config
    import aws_sdk_bedrock_agentcore.types.harness_gemini_model_config
    import aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config
    import aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config


class _HarnessModelConfiguration_bedrockModelConfig(TypedDict):
    bedrockModelConfig: "aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config.HarnessBedrockModelConfig"


class _HarnessModelConfiguration_openAiModelConfig(TypedDict):
    openAiModelConfig: "aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config.HarnessOpenAiModelConfig"


class _HarnessModelConfiguration_geminiModelConfig(TypedDict):
    geminiModelConfig: "aws_sdk_bedrock_agentcore.types.harness_gemini_model_config.HarnessGeminiModelConfig"


class _HarnessModelConfiguration_liteLlmModelConfig(TypedDict):
    liteLlmModelConfig: "aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config.HarnessLiteLlmModelConfig"


HarnessModelConfiguration: TypeAlias = (
    _HarnessModelConfiguration_bedrockModelConfig
    | _HarnessModelConfiguration_openAiModelConfig
    | _HarnessModelConfiguration_geminiModelConfig
    | _HarnessModelConfiguration_liteLlmModelConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessModelConfiguration) -> dict:
    if "bedrockModelConfig" in value:
        import aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config

        return {
            "bedrockModelConfig": aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config.serialize_json(
                value["bedrockModelConfig"]
            )
        }
    elif "openAiModelConfig" in value:
        import aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config

        return {
            "openAiModelConfig": aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config.serialize_json(
                value["openAiModelConfig"]
            )
        }
    elif "geminiModelConfig" in value:
        import aws_sdk_bedrock_agentcore.types.harness_gemini_model_config

        return {
            "geminiModelConfig": aws_sdk_bedrock_agentcore.types.harness_gemini_model_config.serialize_json(
                value["geminiModelConfig"]
            )
        }
    elif "liteLlmModelConfig" in value:
        import aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config

        return {
            "liteLlmModelConfig": aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config.serialize_json(
                value["liteLlmModelConfig"]
            )
        }
    else:
        raise SerializationError("HarnessModelConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessModelConfiguration:
    if "bedrockModelConfig" in data:
        import aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config

        return {
            "bedrockModelConfig": aws_sdk_bedrock_agentcore.types.harness_bedrock_model_config.deserialize_json(
                data["bedrockModelConfig"]
            )
        }
    elif "openAiModelConfig" in data:
        import aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config

        return {
            "openAiModelConfig": aws_sdk_bedrock_agentcore.types.harness_open_ai_model_config.deserialize_json(
                data["openAiModelConfig"]
            )
        }
    elif "geminiModelConfig" in data:
        import aws_sdk_bedrock_agentcore.types.harness_gemini_model_config

        return {
            "geminiModelConfig": aws_sdk_bedrock_agentcore.types.harness_gemini_model_config.deserialize_json(
                data["geminiModelConfig"]
            )
        }
    elif "liteLlmModelConfig" in data:
        import aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config

        return {
            "liteLlmModelConfig": aws_sdk_bedrock_agentcore.types.harness_lite_llm_model_config.deserialize_json(
                data["liteLlmModelConfig"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessModelConfiguration: no recognized variant key"
        )
