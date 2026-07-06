"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessGeminiModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.api_key_arn
    import aws_sdk_bedrock_agentcore_control.types.max_tokens
    import aws_sdk_bedrock_agentcore_control.types.model_id
    import aws_sdk_bedrock_agentcore_control.types.temperature
    import aws_sdk_bedrock_agentcore_control.types.top_k
    import aws_sdk_bedrock_agentcore_control.types.top_p


class HarnessGeminiModelConfig(TypedDict, closed=True):
    model_id: "aws_sdk_bedrock_agentcore_control.types.model_id.ModelId"
    """<p>The Gemini model ID.</p>"""
    api_key_arn: "aws_sdk_bedrock_agentcore_control.types.api_key_arn.ApiKeyArn"
    """<p>The ARN of your Gemini API key on AgentCore Identity.</p>"""
    max_tokens: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_tokens.MaxTokens"
    ]
    """<p>The maximum number of tokens to allow in the generated response per model call.</p>"""
    temperature: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.temperature.Temperature"
    ]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["aws_sdk_bedrock_agentcore_control.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    top_k: NotRequired["aws_sdk_bedrock_agentcore_control.types.top_k.TopK"]
    """<p>The topK set when calling the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessGeminiModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    out["apiKeyArn"] = value["api_key_arn"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "top_k" in value:
        out["topK"] = value["top_k"]
    return out


def deserialize_json(data: dict) -> HarnessGeminiModelConfig:
    out: HarnessGeminiModelConfig = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("HarnessGeminiModelConfig.model_id required")
    if "apiKeyArn" in data:
        out["api_key_arn"] = data["apiKeyArn"]
    else:
        raise DeserializationError("HarnessGeminiModelConfig.api_key_arn required")
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "topK" in data:
        out["top_k"] = data["topK"]
    return out
