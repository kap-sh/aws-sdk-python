"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ReasoningContentBlockDelta``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _ReasoningContentBlockDelta_text(TypedDict):
    text: "str"


class _ReasoningContentBlockDelta_redactedContent(TypedDict):
    redactedContent: "bytes"


class _ReasoningContentBlockDelta_signature(TypedDict):
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
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": aws_sdk_bedrock_runtime.types._prelude.blob.serialize_json(
                value["redactedContent"]
            )
        }
    elif "signature" in value:
        return {"signature": value["signature"]}
    else:
        raise SerializationError("ReasoningContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> ReasoningContentBlockDelta:
    if "text" in data:
        return {"text": data["text"]}
    elif "redactedContent" in data:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": aws_sdk_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["redactedContent"]
            )
        }
    elif "signature" in data:
        return {"signature": data["signature"]}
    else:
        raise DeserializationError(
            "ReasoningContentBlockDelta: no recognized variant key"
        )
