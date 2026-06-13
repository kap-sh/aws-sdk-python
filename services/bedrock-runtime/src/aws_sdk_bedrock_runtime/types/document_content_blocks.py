"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.document_content_block

DocumentContentBlocks: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.document_content_block.DocumentContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContentBlocks) -> list:
    import aws_sdk_bedrock_runtime.types.document_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.document_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentContentBlocks:
    import aws_sdk_bedrock_runtime.types.document_content_block

    out: DocumentContentBlocks = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.document_content_block.deserialize_json(item)
        )
    return out
