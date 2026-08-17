"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.document_content_block

DocumentContentBlocks: TypeAlias = list[
    "capo_bedrock_runtime.types.document_content_block.DocumentContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContentBlocks) -> list:
    import capo_bedrock_runtime.types.document_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.document_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentContentBlocks:
    import capo_bedrock_runtime.types.document_content_block

    out: DocumentContentBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.document_content_block.deserialize_json(item)
        )
    return out
