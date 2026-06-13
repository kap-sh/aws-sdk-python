"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ReasoningContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.reasoning_text_block


class _ReasoningContentBlock_reasoningText(TypedDict):
    reasoningText: (
        "aws_sdk_bedrock_runtime.types.reasoning_text_block.ReasoningTextBlock"
    )


class _ReasoningContentBlock_redactedContent(TypedDict):
    redactedContent: "bytes"


ReasoningContentBlock: TypeAlias = (
    _ReasoningContentBlock_reasoningText | _ReasoningContentBlock_redactedContent
)


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningContentBlock) -> dict:
    if "reasoningText" in value:
        import aws_sdk_bedrock_runtime.types.reasoning_text_block

        return {
            "reasoningText": aws_sdk_bedrock_runtime.types.reasoning_text_block.serialize_json(
                value["reasoningText"]
            )
        }
    elif "redactedContent" in value:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": aws_sdk_bedrock_runtime.types._prelude.blob.serialize_json(
                value["redactedContent"]
            )
        }
    else:
        raise SerializationError("ReasoningContentBlock: no variant present")


def deserialize_json(data: dict) -> ReasoningContentBlock:
    if "reasoningText" in data:
        import aws_sdk_bedrock_runtime.types.reasoning_text_block

        return {
            "reasoningText": aws_sdk_bedrock_runtime.types.reasoning_text_block.deserialize_json(
                data["reasoningText"]
            )
        }
    elif "redactedContent" in data:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "redactedContent": aws_sdk_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["redactedContent"]
            )
        }
    else:
        raise DeserializationError("ReasoningContentBlock: no recognized variant key")
