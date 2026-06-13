"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citation_source_content

CitationSourceContentList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.citation_source_content.CitationSourceContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CitationSourceContentList) -> list:
    import aws_sdk_bedrock_runtime.types.citation_source_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.citation_source_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CitationSourceContentList:
    import aws_sdk_bedrock_runtime.types.citation_source_content

    out: CitationSourceContentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.citation_source_content.deserialize_json(item)
        )
    return out
