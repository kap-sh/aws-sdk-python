"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.integer
    import aws_sdk_qbusiness.types.snippet_excerpt
    import aws_sdk_qbusiness.types.source_attribution_media_id
    import aws_sdk_qbusiness.types.source_details
    import aws_sdk_qbusiness.types.string


class TextSegment(TypedDict):
    begin_offset: NotRequired["aws_sdk_qbusiness.types.integer.Integer"]
    """<p>The zero-based location in the response string where the source attribution starts.</p>"""
    end_offset: NotRequired["aws_sdk_qbusiness.types.integer.Integer"]
    """<p>The zero-based location in the response string where the source attribution ends.</p>"""
    snippet_excerpt: NotRequired[
        "aws_sdk_qbusiness.types.snippet_excerpt.SnippetExcerpt"
    ]
    """<p>The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q Business chat response.</p>"""
    media_id: NotRequired[
        "aws_sdk_qbusiness.types.source_attribution_media_id.SourceAttributionMediaId"
    ]
    """<p>The identifier of the media object associated with the text segment in the source attribution.</p>"""
    media_mime_type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The MIME type (image/png) of the media object associated with the text segment in the source attribution.</p>"""
    source_details: NotRequired["aws_sdk_qbusiness.types.source_details.SourceDetails"]
    """<p>Source information for a segment of extracted text, including its media type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextSegment) -> dict:
    out: dict = {}
    if "begin_offset" in value:
        out["beginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["endOffset"] = value["end_offset"]
    if "snippet_excerpt" in value:
        import aws_sdk_qbusiness.types.snippet_excerpt

        out["snippetExcerpt"] = aws_sdk_qbusiness.types.snippet_excerpt.serialize_json(
            value["snippet_excerpt"]
        )
    if "media_id" in value:
        out["mediaId"] = value["media_id"]
    if "media_mime_type" in value:
        out["mediaMimeType"] = value["media_mime_type"]
    if "source_details" in value:
        import aws_sdk_qbusiness.types.source_details

        out["sourceDetails"] = aws_sdk_qbusiness.types.source_details.serialize_json(
            value["source_details"]
        )
    return out


def deserialize_json(data: dict) -> TextSegment:
    out: TextSegment = {}  # type: ignore[typeddict-item]
    if "beginOffset" in data:
        out["begin_offset"] = data["beginOffset"]
    if "endOffset" in data:
        out["end_offset"] = data["endOffset"]
    if "snippetExcerpt" in data:
        import aws_sdk_qbusiness.types.snippet_excerpt

        out["snippet_excerpt"] = (
            aws_sdk_qbusiness.types.snippet_excerpt.deserialize_json(
                data["snippetExcerpt"]
            )
        )
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    if "mediaMimeType" in data:
        out["media_mime_type"] = data["mediaMimeType"]
    if "sourceDetails" in data:
        import aws_sdk_qbusiness.types.source_details

        out["source_details"] = aws_sdk_qbusiness.types.source_details.deserialize_json(
            data["sourceDetails"]
        )
    return out
