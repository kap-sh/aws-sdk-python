"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.document_block
    import aws_sdk_bedrock_runtime.types.image_block
    import aws_sdk_bedrock_runtime.types.search_result_block
    import aws_sdk_bedrock_runtime.types.video_block


class _ToolResultContentBlock_json(TypedDict):
    json: "object"


class _ToolResultContentBlock_text(TypedDict):
    text: "str"


class _ToolResultContentBlock_image(TypedDict):
    image: "aws_sdk_bedrock_runtime.types.image_block.ImageBlock"


class _ToolResultContentBlock_document(TypedDict):
    document: "aws_sdk_bedrock_runtime.types.document_block.DocumentBlock"


class _ToolResultContentBlock_video(TypedDict):
    video: "aws_sdk_bedrock_runtime.types.video_block.VideoBlock"


class _ToolResultContentBlock_searchResult(TypedDict):
    searchResult: "aws_sdk_bedrock_runtime.types.search_result_block.SearchResultBlock"


ToolResultContentBlock: TypeAlias = (
    _ToolResultContentBlock_json
    | _ToolResultContentBlock_text
    | _ToolResultContentBlock_image
    | _ToolResultContentBlock_document
    | _ToolResultContentBlock_video
    | _ToolResultContentBlock_searchResult
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultContentBlock) -> dict:
    if "json" in value:
        return {"json": value["json"]}
    elif "text" in value:
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
    elif "searchResult" in value:
        import aws_sdk_bedrock_runtime.types.search_result_block

        return {
            "searchResult": aws_sdk_bedrock_runtime.types.search_result_block.serialize_json(
                value["searchResult"]
            )
        }
    else:
        raise SerializationError("ToolResultContentBlock: no variant present")


def deserialize_json(data: dict) -> ToolResultContentBlock:
    if "json" in data:
        return {"json": data["json"]}
    elif "text" in data:
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
    elif "searchResult" in data:
        import aws_sdk_bedrock_runtime.types.search_result_block

        return {
            "searchResult": aws_sdk_bedrock_runtime.types.search_result_block.deserialize_json(
                data["searchResult"]
            )
        }
    else:
        raise DeserializationError("ToolResultContentBlock: no recognized variant key")
