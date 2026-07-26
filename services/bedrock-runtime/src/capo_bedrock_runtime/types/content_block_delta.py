"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citations_delta
    import capo_bedrock_runtime.types.image_block_delta
    import capo_bedrock_runtime.types.reasoning_content_block_delta
    import capo_bedrock_runtime.types.tool_result_blocks_delta
    import capo_bedrock_runtime.types.tool_use_block_delta


class _ContentBlockDelta_text(TypedDict, closed=True):
    text: "str"


class _ContentBlockDelta_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_runtime.types.tool_use_block_delta.ToolUseBlockDelta"


class _ContentBlockDelta_toolResult(TypedDict, closed=True):
    toolResult: (
        "capo_bedrock_runtime.types.tool_result_blocks_delta.ToolResultBlocksDelta"
    )


class _ContentBlockDelta_reasoningContent(TypedDict, closed=True):
    reasoningContent: "capo_bedrock_runtime.types.reasoning_content_block_delta.ReasoningContentBlockDelta"


class _ContentBlockDelta_citation(TypedDict, closed=True):
    citation: "capo_bedrock_runtime.types.citations_delta.CitationsDelta"


class _ContentBlockDelta_image(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block_delta.ImageBlockDelta"


ContentBlockDelta: TypeAlias = (
    _ContentBlockDelta_text
    | _ContentBlockDelta_toolUse
    | _ContentBlockDelta_toolResult
    | _ContentBlockDelta_reasoningContent
    | _ContentBlockDelta_citation
    | _ContentBlockDelta_image
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import capo_bedrock_runtime.types.tool_use_block_delta

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_delta.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_blocks_delta.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_runtime.types.reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block_delta.serialize_json(
                value["reasoningContent"]
            )
        }
    elif "citation" in value:
        import capo_bedrock_runtime.types.citations_delta

        return {
            "citation": capo_bedrock_runtime.types.citations_delta.serialize_json(
                value["citation"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.image_block_delta

        return {
            "image": capo_bedrock_runtime.types.image_block_delta.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("ContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> ContentBlockDelta:
    if "text" in data:
        return {"text": data["text"]}
    elif "toolUse" in data:
        import capo_bedrock_runtime.types.tool_use_block_delta

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_delta.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import capo_bedrock_runtime.types.tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_blocks_delta.deserialize_json(
                data["toolResult"]
            )
        }
    elif "reasoningContent" in data:
        import capo_bedrock_runtime.types.reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block_delta.deserialize_json(
                data["reasoningContent"]
            )
        }
    elif "citation" in data:
        import capo_bedrock_runtime.types.citations_delta

        return {
            "citation": capo_bedrock_runtime.types.citations_delta.deserialize_json(
                data["citation"]
            )
        }
    elif "image" in data:
        import capo_bedrock_runtime.types.image_block_delta

        return {
            "image": capo_bedrock_runtime.types.image_block_delta.deserialize_json(
                data["image"]
            )
        }
    else:
        raise DeserializationError("ContentBlockDelta: no recognized variant key")
