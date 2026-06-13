"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockDeltaEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.content_block_delta
    import aws_sdk_bedrock_runtime.types.non_negative_integer


class ContentBlockDeltaEvent(TypedDict):
    delta: "aws_sdk_bedrock_runtime.types.content_block_delta.ContentBlockDelta"
    """<p>The delta for a content block delta event.</p>"""
    content_block_index: (
        "aws_sdk_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The block index for a content block delta event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockDeltaEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.content_block_delta

    out["delta"] = aws_sdk_bedrock_runtime.types.content_block_delta.serialize_json(
        value["delta"]
    )
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockDeltaEvent:
    out: ContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if "delta" in data:
        import aws_sdk_bedrock_runtime.types.content_block_delta

        out["delta"] = (
            aws_sdk_bedrock_runtime.types.content_block_delta.deserialize_json(
                data["delta"]
            )
        )
    else:
        raise DeserializationError("ContentBlockDeltaEvent.delta required")
    if "contentBlockIndex" in data:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "ContentBlockDeltaEvent.content_block_index required"
        )
    return out
