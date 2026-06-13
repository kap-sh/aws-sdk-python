"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourceApiKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.api_key_type

class GetResourceApiKeyResponse(TypedDict):
    api_key: "aws_sdk_bedrock_agentcore.types.api_key_type.ApiKeyType"
    """<p>The API key associated with the resource requested.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetResourceApiKeyResponse) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> GetResourceApiKeyResponse:
    out: GetResourceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("GetResourceApiKeyResponse.api_key required")
    return out