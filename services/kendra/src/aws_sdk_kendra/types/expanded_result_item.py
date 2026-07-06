"""Generated from Smithy shape ``com.amazonaws.kendra#ExpandedResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_list
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.result_id
    import aws_sdk_kendra.types.text_with_highlights
    import aws_sdk_kendra.types.url


class ExpandedResultItem(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.result_id.ResultId"]
    """<p>The identifier for the expanded result.</p>"""
    document_id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The idenitifier of the document.</p>"""
    document_title: NotRequired[
        "aws_sdk_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    document_excerpt: NotRequired[
        "aws_sdk_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    document_uri: NotRequired["aws_sdk_kendra.types.url.Url"]
    """<p>The URI of the original location of the document.</p>"""
    document_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    r"""<p>An array of document attributes assigned to a document in the search results. For example, the document author (\"_author\") or the source URI (\"_source_uri\") of the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpandedResultItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "document_title" in value:
        import aws_sdk_kendra.types.text_with_highlights

        out["DocumentTitle"] = (
            aws_sdk_kendra.types.text_with_highlights.serialize_aws_json_1_1(
                value["document_title"]
            )
        )
    if "document_excerpt" in value:
        import aws_sdk_kendra.types.text_with_highlights

        out["DocumentExcerpt"] = (
            aws_sdk_kendra.types.text_with_highlights.serialize_aws_json_1_1(
                value["document_excerpt"]
            )
        )
    if "document_uri" in value:
        out["DocumentURI"] = value["document_uri"]
    if "document_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_list

        out["DocumentAttributes"] = (
            aws_sdk_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["document_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpandedResultItem:
    out: ExpandedResultItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "DocumentTitle" in data:
        import aws_sdk_kendra.types.text_with_highlights

        out["document_title"] = (
            aws_sdk_kendra.types.text_with_highlights.deserialize_aws_json_1_1(
                data["DocumentTitle"]
            )
        )
    if "DocumentExcerpt" in data:
        import aws_sdk_kendra.types.text_with_highlights

        out["document_excerpt"] = (
            aws_sdk_kendra.types.text_with_highlights.deserialize_aws_json_1_1(
                data["DocumentExcerpt"]
            )
        )
    if "DocumentURI" in data:
        out["document_uri"] = data["DocumentURI"]
    if "DocumentAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_list

        out["document_attributes"] = (
            aws_sdk_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["DocumentAttributes"]
            )
        )
    return out
