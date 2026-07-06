"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Citation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citation_location
    import aws_sdk_bedrock_runtime.types.citation_source_content_list


class Citation(TypedDict, closed=True):
    title: NotRequired["str"]
    """<p>The title or identifier of the source document being cited.</p>"""
    source: NotRequired["str"]
    """<p>The source from the original search result that provided the cited content.</p>"""
    source_content: NotRequired[
        "aws_sdk_bedrock_runtime.types.citation_source_content_list.CitationSourceContentList"
    ]
    """<p>The specific content from the source document that was referenced or cited in the generated response.</p>"""
    location: NotRequired[
        "aws_sdk_bedrock_runtime.types.citation_location.CitationLocation"
    ]
    """<p>The precise location within the source document where the cited content can be found, including character positions, page numbers, or chunk identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "source" in value:
        out["source"] = value["source"]
    if "source_content" in value:
        import aws_sdk_bedrock_runtime.types.citation_source_content_list

        out["sourceContent"] = (
            aws_sdk_bedrock_runtime.types.citation_source_content_list.serialize_json(
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


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "source" in data:
        out["source"] = data["source"]
    if "sourceContent" in data:
        import aws_sdk_bedrock_runtime.types.citation_source_content_list

        out["source_content"] = (
            aws_sdk_bedrock_runtime.types.citation_source_content_list.deserialize_json(
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
