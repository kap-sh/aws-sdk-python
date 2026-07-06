"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessBedrockModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format
    import aws_sdk_bedrock_agentcore.types.max_tokens
    import aws_sdk_bedrock_agentcore.types.model_id
    import aws_sdk_bedrock_agentcore.types.temperature
    import aws_sdk_bedrock_agentcore.types.top_p


class HarnessBedrockModelConfig(TypedDict, closed=True):
    model_id: "aws_sdk_bedrock_agentcore.types.model_id.ModelId"
    """<p>The Bedrock model ID.</p>"""
    max_tokens: NotRequired["aws_sdk_bedrock_agentcore.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per iteration.</p>"""
    temperature: NotRequired["aws_sdk_bedrock_agentcore.types.temperature.Temperature"]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["aws_sdk_bedrock_agentcore.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    api_format: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format.HarnessBedrockApiFormat"
    ]
    """<p>The API format to use when calling the Bedrock provider.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessBedrockModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "api_format" in value:
        import aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format

        out["apiFormat"] = (
            aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format.serialize_json(
                value["api_format"]
            )
        )
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessBedrockModelConfig:
    out: HarnessBedrockModelConfig = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("HarnessBedrockModelConfig.model_id required")
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "apiFormat" in data:
        import aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format

        out["api_format"] = (
            aws_sdk_bedrock_agentcore.types.harness_bedrock_api_format.deserialize_json(
                data["apiFormat"]
            )
        )
    if "additionalParams" in data:
        out["additional_params"] = data["additionalParams"]
    return out
