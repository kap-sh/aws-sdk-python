"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSystemContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class _HarnessSystemContentBlock_text(TypedDict):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"


HarnessSystemContentBlock: TypeAlias = _HarnessSystemContentBlock_text


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSystemContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("HarnessSystemContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessSystemContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError(
            "HarnessSystemContentBlock: no recognized variant key"
        )
