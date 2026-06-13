"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.audio_block
    import aws_sdk_bedrock_runtime.types.cache_point_block
    import aws_sdk_bedrock_runtime.types.citations_content_block
    import aws_sdk_bedrock_runtime.types.document_block
    import aws_sdk_bedrock_runtime.types.guardrail_converse_content_block
    import aws_sdk_bedrock_runtime.types.image_block
    import aws_sdk_bedrock_runtime.types.reasoning_content_block
    import aws_sdk_bedrock_runtime.types.search_result_block
    import aws_sdk_bedrock_runtime.types.tool_result_block
    import aws_sdk_bedrock_runtime.types.tool_use_block
    import aws_sdk_bedrock_runtime.types.video_block


class _ContentBlock_text(TypedDict):
    text: "str"


class _ContentBlock_image(TypedDict):
    image: "aws_sdk_bedrock_runtime.types.image_block.ImageBlock"


class _ContentBlock_document(TypedDict):
    document: "aws_sdk_bedrock_runtime.types.document_block.DocumentBlock"


class _ContentBlock_video(TypedDict):
    video: "aws_sdk_bedrock_runtime.types.video_block.VideoBlock"


class _ContentBlock_audio(TypedDict):
    audio: "aws_sdk_bedrock_runtime.types.audio_block.AudioBlock"


class _ContentBlock_toolUse(TypedDict):
    toolUse: "aws_sdk_bedrock_runtime.types.tool_use_block.ToolUseBlock"


class _ContentBlock_toolResult(TypedDict):
    toolResult: "aws_sdk_bedrock_runtime.types.tool_result_block.ToolResultBlock"


class _ContentBlock_guardContent(TypedDict):
    guardContent: "aws_sdk_bedrock_runtime.types.guardrail_converse_content_block.GuardrailConverseContentBlock"


class _ContentBlock_cachePoint(TypedDict):
    cachePoint: "aws_sdk_bedrock_runtime.types.cache_point_block.CachePointBlock"


class _ContentBlock_reasoningContent(TypedDict):
    reasoningContent: (
        "aws_sdk_bedrock_runtime.types.reasoning_content_block.ReasoningContentBlock"
    )


class _ContentBlock_citationsContent(TypedDict):
    citationsContent: (
        "aws_sdk_bedrock_runtime.types.citations_content_block.CitationsContentBlock"
    )


class _ContentBlock_searchResult(TypedDict):
    searchResult: "aws_sdk_bedrock_runtime.types.search_result_block.SearchResultBlock"


ContentBlock: TypeAlias = (
    _ContentBlock_text
    | _ContentBlock_image
    | _ContentBlock_document
    | _ContentBlock_video
    | _ContentBlock_audio
    | _ContentBlock_toolUse
    | _ContentBlock_toolResult
    | _ContentBlock_guardContent
    | _ContentBlock_cachePoint
    | _ContentBlock_reasoningContent
    | _ContentBlock_citationsContent
    | _ContentBlock_searchResult
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "image" in value:
        import aws_sdk_bedrock_runtime.types.image_block

        return {
            "image": aws_sdk_bedrock_runtime.types.image_block.serialize_json(
                value["image"]
            )
        }
    elif "document" in value:
        import aws_sdk_bedrock_runtime.types.document_block

        return {
            "document": aws_sdk_bedrock_runtime.types.document_block.serialize_json(
                value["document"]
            )
        }
    elif "video" in value:
        import aws_sdk_bedrock_runtime.types.video_block

        return {
            "video": aws_sdk_bedrock_runtime.types.video_block.serialize_json(
                value["video"]
            )
        }
    elif "audio" in value:
        import aws_sdk_bedrock_runtime.types.audio_block

        return {
            "audio": aws_sdk_bedrock_runtime.types.audio_block.serialize_json(
                value["audio"]
            )
        }
    elif "toolUse" in value:
        import aws_sdk_bedrock_runtime.types.tool_use_block

        return {
            "toolUse": aws_sdk_bedrock_runtime.types.tool_use_block.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import aws_sdk_bedrock_runtime.types.tool_result_block

        return {
            "toolResult": aws_sdk_bedrock_runtime.types.tool_result_block.serialize_json(
                value["toolResult"]
            )
        }
    elif "guardContent" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_content_block

        return {
            "guardContent": aws_sdk_bedrock_runtime.types.guardrail_converse_content_block.serialize_json(
                value["guardContent"]
            )
        }
    elif "cachePoint" in value:
        import aws_sdk_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": aws_sdk_bedrock_runtime.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    elif "reasoningContent" in value:
        import aws_sdk_bedrock_runtime.types.reasoning_content_block

        return {
            "reasoningContent": aws_sdk_bedrock_runtime.types.reasoning_content_block.serialize_json(
                value["reasoningContent"]
            )
        }
    elif "citationsContent" in value:
        import aws_sdk_bedrock_runtime.types.citations_content_block

        return {
            "citationsContent": aws_sdk_bedrock_runtime.types.citations_content_block.serialize_json(
                value["citationsContent"]
            )
        }
    elif "searchResult" in value:
        import aws_sdk_bedrock_runtime.types.search_result_block

        return {
            "searchResult": aws_sdk_bedrock_runtime.types.search_result_block.serialize_json(
                value["searchResult"]
            )
        }
    else:
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "image" in data:
        import aws_sdk_bedrock_runtime.types.image_block

        return {
            "image": aws_sdk_bedrock_runtime.types.image_block.deserialize_json(
                data["image"]
            )
        }
    elif "document" in data:
        import aws_sdk_bedrock_runtime.types.document_block

        return {
            "document": aws_sdk_bedrock_runtime.types.document_block.deserialize_json(
                data["document"]
            )
        }
    elif "video" in data:
        import aws_sdk_bedrock_runtime.types.video_block

        return {
            "video": aws_sdk_bedrock_runtime.types.video_block.deserialize_json(
                data["video"]
            )
        }
    elif "audio" in data:
        import aws_sdk_bedrock_runtime.types.audio_block

        return {
            "audio": aws_sdk_bedrock_runtime.types.audio_block.deserialize_json(
                data["audio"]
            )
        }
    elif "toolUse" in data:
        import aws_sdk_bedrock_runtime.types.tool_use_block

        return {
            "toolUse": aws_sdk_bedrock_runtime.types.tool_use_block.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import aws_sdk_bedrock_runtime.types.tool_result_block

        return {
            "toolResult": aws_sdk_bedrock_runtime.types.tool_result_block.deserialize_json(
                data["toolResult"]
            )
        }
    elif "guardContent" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_content_block

        return {
            "guardContent": aws_sdk_bedrock_runtime.types.guardrail_converse_content_block.deserialize_json(
                data["guardContent"]
            )
        }
    elif "cachePoint" in data:
        import aws_sdk_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": aws_sdk_bedrock_runtime.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    elif "reasoningContent" in data:
        import aws_sdk_bedrock_runtime.types.reasoning_content_block

        return {
            "reasoningContent": aws_sdk_bedrock_runtime.types.reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        }
    elif "citationsContent" in data:
        import aws_sdk_bedrock_runtime.types.citations_content_block

        return {
            "citationsContent": aws_sdk_bedrock_runtime.types.citations_content_block.deserialize_json(
                data["citationsContent"]
            )
        }
    elif "searchResult" in data:
        import aws_sdk_bedrock_runtime.types.search_result_block

        return {
            "searchResult": aws_sdk_bedrock_runtime.types.search_result_block.deserialize_json(
                data["searchResult"]
            )
        }
    else:
        raise DeserializationError("ContentBlock: no recognized variant key")
