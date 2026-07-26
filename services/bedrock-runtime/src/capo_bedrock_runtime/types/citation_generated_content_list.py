"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationGeneratedContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citation_generated_content

CitationGeneratedContentList: TypeAlias = list[
    "capo_bedrock_runtime.types.citation_generated_content.CitationGeneratedContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CitationGeneratedContentList) -> list:
    import capo_bedrock_runtime.types.citation_generated_content

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.citation_generated_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CitationGeneratedContentList:
    import capo_bedrock_runtime.types.citation_generated_content

    out: CitationGeneratedContentList = []
    for item in data:
        out.append(
            capo_bedrock_runtime.types.citation_generated_content.deserialize_json(item)
        )
    return out
