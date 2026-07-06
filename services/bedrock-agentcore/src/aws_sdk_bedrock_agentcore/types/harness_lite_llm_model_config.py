"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessLiteLlmModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.api_key_arn
    import aws_sdk_bedrock_agentcore.types.harness_lite_llm_api_base
    import aws_sdk_bedrock_agentcore.types.max_tokens
    import aws_sdk_bedrock_agentcore.types.model_id
    import aws_sdk_bedrock_agentcore.types.temperature
    import aws_sdk_bedrock_agentcore.types.top_p


class HarnessLiteLlmModelConfig(TypedDict, closed=True):
    model_id: "aws_sdk_bedrock_agentcore.types.model_id.ModelId"
    r"""<p>The LiteLLM model identifier (e.g., \"anthropic/claude-3-sonnet\").</p>"""
    api_key_arn: NotRequired["aws_sdk_bedrock_agentcore.types.api_key_arn.ApiKeyArn"]
    """<p>The ARN of the API key in AgentCore Identity for authenticating with the model provider.</p>"""
    api_base: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_lite_llm_api_base.HarnessLiteLlmApiBase"
    ]
    """<p>The base URL for the model provider's API endpoint.</p>"""
    max_tokens: NotRequired["aws_sdk_bedrock_agentcore.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per iteration.</p>"""
    temperature: NotRequired["aws_sdk_bedrock_agentcore.types.temperature.Temperature"]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["aws_sdk_bedrock_agentcore.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessLiteLlmModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "api_key_arn" in value:
        out["apiKeyArn"] = value["api_key_arn"]
    if "api_base" in value:
        out["apiBase"] = value["api_base"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessLiteLlmModelConfig:
    out: HarnessLiteLlmModelConfig = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("HarnessLiteLlmModelConfig.model_id required")
    if "apiKeyArn" in data:
        out["api_key_arn"] = data["apiKeyArn"]
    if "apiBase" in data:
        out["api_base"] = data["apiBase"]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "additionalParams" in data:
        out["additional_params"] = data["additionalParams"]
    return out
