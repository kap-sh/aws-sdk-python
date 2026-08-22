"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ContentBlock``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError


class _ContentBlock_text(TypedDict, closed=True):
    text: "str"


ContentBlock: TypeAlias = _ContentBlock_text


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError("ContentBlock: no recognized variant key")
