"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ReasoningContentBlockDelta``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError


class _ReasoningContentBlockDelta_text(TypedDict, closed=True):
    text: "str"


class _ReasoningContentBlockDelta_redactedContent(TypedDict, closed=True):
    redactedContent: "bytes"


class _ReasoningContentBlockDelta_signature(TypedDict, closed=True):
    signature: "str"


ReasoningContentBlockDelta: TypeAlias = (
    _ReasoningContentBlockDelta_text
    | _ReasoningContentBlockDelta_redactedContent
    | _ReasoningContentBlockDelta_signature
)


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningContentBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "redactedContent" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["redactedContent"]
            )
        }
    elif "signature" in value:
        return {"signature": value["signature"]}
    else:
        raise SerializationError("ReasoningContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> ReasoningContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("redactedContent") is not None:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["redactedContent"]
            )
        }
    elif data.get("signature") is not None:
        return {"signature": data["signature"]}
    else:
        raise DeserializationError(
            "ReasoningContentBlockDelta: no recognized variant key"
        )
