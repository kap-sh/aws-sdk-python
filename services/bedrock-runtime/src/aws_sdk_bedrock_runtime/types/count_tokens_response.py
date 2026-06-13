"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CountTokensResponse``."""

from typing import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError


class CountTokensResponse(TypedDict):
    input_tokens: "int"
    """<p>The number of tokens in the provided input according to the specified model's tokenization rules. This count represents the number of input tokens that would be processed if the same input were sent to the model in an inference request. Use this value to estimate costs and ensure your inputs stay within model token limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CountTokensResponse) -> dict:
    out: dict = {}
    out["inputTokens"] = value["input_tokens"]
    return out


def deserialize_json(data: dict) -> CountTokensResponse:
    out: CountTokensResponse = {}  # type: ignore[typeddict-item]
    if "inputTokens" in data:
        out["input_tokens"] = data["inputTokens"]
    else:
        raise DeserializationError("CountTokensResponse.input_tokens required")
    return out
