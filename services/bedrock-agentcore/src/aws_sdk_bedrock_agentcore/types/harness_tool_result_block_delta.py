"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_json
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class _HarnessToolResultBlockDelta_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessToolResultBlockDelta_json(TypedDict, closed=True):
    json: "aws_sdk_bedrock_agentcore.types.sensitive_json.SensitiveJson"


HarnessToolResultBlockDelta: TypeAlias = (
    _HarnessToolResultBlockDelta_text | _HarnessToolResultBlockDelta_json
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("HarnessToolResultBlockDelta: no variant present")


def deserialize_json(data: dict) -> HarnessToolResultBlockDelta:
    if "text" in data:
        return {"text": data["text"]}
    elif "json" in data:
        return {"json": data["json"]}
    else:
        raise DeserializationError(
            "HarnessToolResultBlockDelta: no recognized variant key"
        )
