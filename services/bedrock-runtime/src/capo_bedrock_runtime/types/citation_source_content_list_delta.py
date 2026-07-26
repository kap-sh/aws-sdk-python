"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContentListDelta``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citation_source_content_delta

CitationSourceContentListDelta: TypeAlias = list[
    "capo_bedrock_runtime.types.citation_source_content_delta.CitationSourceContentDelta"
]


# --- restJson1 ser/de ---
def serialize_json(value: CitationSourceContentListDelta) -> list:
    import capo_bedrock_runtime.types.citation_source_content_delta

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.citation_source_content_delta.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CitationSourceContentListDelta:
    import capo_bedrock_runtime.types.citation_source_content_delta

    out: CitationSourceContentListDelta = []
    for item in data:
        out.append(
            capo_bedrock_runtime.types.citation_source_content_delta.deserialize_json(
                item
            )
        )
    return out
