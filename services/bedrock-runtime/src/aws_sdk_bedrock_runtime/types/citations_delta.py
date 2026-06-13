"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationsDelta``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citation_location
    import aws_sdk_bedrock_runtime.types.citation_source_content_list_delta


class CitationsDelta(TypedDict):
    title: NotRequired["str"]
    """<p>The title or identifier of the source document being cited.</p>"""
    source: NotRequired["str"]
    """<p>The source from the original search result that provided the cited content.</p>"""
    source_content: NotRequired[
        "aws_sdk_bedrock_runtime.types.citation_source_content_list_delta.CitationSourceContentListDelta"
    ]
    """<p>The specific content from the source document that was referenced or cited in the generated response.</p>"""
    location: NotRequired[
        "aws_sdk_bedrock_runtime.types.citation_location.CitationLocation"
    ]
    """<p>Specifies the precise location within a source document where cited content can be found. This can include character-level positions, page numbers, or document chunks depending on the document type and indexing method.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationsDelta) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "source" in value:
        out["source"] = value["source"]
    if "source_content" in value:
        import aws_sdk_bedrock_runtime.types.citation_source_content_list_delta

        out["sourceContent"] = (
            aws_sdk_bedrock_runtime.types.citation_source_content_list_delta.serialize_json(
                value["source_content"]
            )
        )
    if "location" in value:
        import aws_sdk_bedrock_runtime.types.citation_location

        out["location"] = (
            aws_sdk_bedrock_runtime.types.citation_location.serialize_json(
                value["location"]
            )
        )
    return out


def deserialize_json(data: dict) -> CitationsDelta:
    out: CitationsDelta = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "source" in data:
        out["source"] = data["source"]
    if "sourceContent" in data:
        import aws_sdk_bedrock_runtime.types.citation_source_content_list_delta

        out["source_content"] = (
            aws_sdk_bedrock_runtime.types.citation_source_content_list_delta.deserialize_json(
                data["sourceContent"]
            )
        )
    if "location" in data:
        import aws_sdk_bedrock_runtime.types.citation_location

        out["location"] = (
            aws_sdk_bedrock_runtime.types.citation_location.deserialize_json(
                data["location"]
            )
        )
    return out
