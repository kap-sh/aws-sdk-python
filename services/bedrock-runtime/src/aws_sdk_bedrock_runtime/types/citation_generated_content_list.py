"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationGeneratedContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citation_generated_content

CitationGeneratedContentList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.citation_generated_content.CitationGeneratedContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CitationGeneratedContentList) -> list:
    import aws_sdk_bedrock_runtime.types.citation_generated_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.citation_generated_content.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CitationGeneratedContentList:
    import aws_sdk_bedrock_runtime.types.citation_generated_content

    out: CitationGeneratedContentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.citation_generated_content.deserialize_json(
                item
            )
        )
    return out
