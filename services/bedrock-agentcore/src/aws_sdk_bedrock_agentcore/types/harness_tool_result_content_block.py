"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_json
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class _HarnessToolResultContentBlock_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessToolResultContentBlock_json(TypedDict, closed=True):
    json: "aws_sdk_bedrock_agentcore.types.sensitive_json.SensitiveJson"


HarnessToolResultContentBlock: TypeAlias = (
    _HarnessToolResultContentBlock_text | _HarnessToolResultContentBlock_json
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("HarnessToolResultContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessToolResultContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "json" in data:
        return {"json": data["json"]}
    else:
        raise DeserializationError(
            "HarnessToolResultContentBlock: no recognized variant key"
        )
