"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citations_config
    import aws_sdk_bedrock_runtime.types.search_result_content_blocks


class SearchResultBlock(TypedDict, closed=True):
    source: "str"
    """<p>The source URL or identifier for the content.</p>"""
    title: "str"
    """<p>A descriptive title for the search result.</p>"""
    content: "aws_sdk_bedrock_runtime.types.search_result_content_blocks.SearchResultContentBlocks"
    """<p>An array of search result content block.</p>"""
    citations: NotRequired[
        "aws_sdk_bedrock_runtime.types.citations_config.CitationsConfig"
    ]
    """<p>Configuration setting for citations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultBlock) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["title"] = value["title"]
    import aws_sdk_bedrock_runtime.types.search_result_content_blocks

    out["content"] = (
        aws_sdk_bedrock_runtime.types.search_result_content_blocks.serialize_json(
            value["content"]
        )
    )
    if "citations" in value:
        import aws_sdk_bedrock_runtime.types.citations_config

        out["citations"] = (
            aws_sdk_bedrock_runtime.types.citations_config.serialize_json(
                value["citations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResultBlock:
    out: SearchResultBlock = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SearchResultBlock.source required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("SearchResultBlock.title required")
    if "content" in data:
        import aws_sdk_bedrock_runtime.types.search_result_content_blocks

        out["content"] = (
            aws_sdk_bedrock_runtime.types.search_result_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("SearchResultBlock.content required")
    if "citations" in data:
        import aws_sdk_bedrock_runtime.types.citations_config

        out["citations"] = (
            aws_sdk_bedrock_runtime.types.citations_config.deserialize_json(
                data["citations"]
            )
        )
    return out
