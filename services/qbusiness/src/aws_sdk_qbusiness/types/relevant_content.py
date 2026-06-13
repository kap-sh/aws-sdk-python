"""Generated from Smithy shape ``com.amazonaws.qbusiness#RelevantContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attributes
    import aws_sdk_qbusiness.types.document_id
    import aws_sdk_qbusiness.types.score_attributes
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.title
    import aws_sdk_qbusiness.types.url


class RelevantContent(TypedDict):
    content: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The actual content of the relevant item.</p>"""
    document_id: NotRequired["aws_sdk_qbusiness.types.document_id.DocumentId"]
    """<p>The unique identifier of the document containing the relevant content.</p>"""
    document_title: NotRequired["aws_sdk_qbusiness.types.title.Title"]
    """<p>The title of the document containing the relevant content.</p>"""
    document_uri: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The URI of the document containing the relevant content.</p>"""
    document_attributes: NotRequired[
        "aws_sdk_qbusiness.types.document_attributes.DocumentAttributes"
    ]
    """<p>Additional attributes of the document containing the relevant content.</p>"""
    score_attributes: NotRequired[
        "aws_sdk_qbusiness.types.score_attributes.ScoreAttributes"
    ]
    """<p>Attributes related to the relevance score of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelevantContent) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    if "document_title" in value:
        out["documentTitle"] = value["document_title"]
    if "document_uri" in value:
        out["documentUri"] = value["document_uri"]
    if "document_attributes" in value:
        import aws_sdk_qbusiness.types.document_attributes

        out["documentAttributes"] = (
            aws_sdk_qbusiness.types.document_attributes.serialize_json(
                value["document_attributes"]
            )
        )
    if "score_attributes" in value:
        import aws_sdk_qbusiness.types.score_attributes

        out["scoreAttributes"] = (
            aws_sdk_qbusiness.types.score_attributes.serialize_json(
                value["score_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RelevantContent:
    out: RelevantContent = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    if "documentId" in data:
        out["document_id"] = data["documentId"]
    if "documentTitle" in data:
        out["document_title"] = data["documentTitle"]
    if "documentUri" in data:
        out["document_uri"] = data["documentUri"]
    if "documentAttributes" in data:
        import aws_sdk_qbusiness.types.document_attributes

        out["document_attributes"] = (
            aws_sdk_qbusiness.types.document_attributes.deserialize_json(
                data["documentAttributes"]
            )
        )
    if "scoreAttributes" in data:
        import aws_sdk_qbusiness.types.score_attributes

        out["score_attributes"] = (
            aws_sdk_qbusiness.types.score_attributes.deserialize_json(
                data["scoreAttributes"]
            )
        )
    return out
