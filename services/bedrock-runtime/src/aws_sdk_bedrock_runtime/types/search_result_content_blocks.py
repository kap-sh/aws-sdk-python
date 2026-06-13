"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.search_result_content_block

SearchResultContentBlocks: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.search_result_content_block.SearchResultContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultContentBlocks) -> list:
    import aws_sdk_bedrock_runtime.types.search_result_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.search_result_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchResultContentBlocks:
    import aws_sdk_bedrock_runtime.types.search_result_content_block

    out: SearchResultContentBlocks = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.search_result_content_block.deserialize_json(
                item
            )
        )
    return out
