"""Generated from Smithy shape ``com.amazonaws.kendra#RetrieveResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.content
    import aws_sdk_kendra.types.document_attribute_list
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.document_title
    import aws_sdk_kendra.types.result_id
    import aws_sdk_kendra.types.score_attributes
    import aws_sdk_kendra.types.url


class RetrieveResultItem(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.result_id.ResultId"]
    """<p>The identifier of the relevant passage result.</p>"""
    document_id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document.</p>"""
    document_title: NotRequired["aws_sdk_kendra.types.document_title.DocumentTitle"]
    """<p>The title of the document.</p>"""
    content: NotRequired["aws_sdk_kendra.types.content.Content"]
    """<p>The contents of the relevant passage.</p>"""
    document_uri: NotRequired["aws_sdk_kendra.types.url.Url"]
    """<p>The URI of the original location of the document.</p>"""
    document_attributes: NotRequired[
        "aws_sdk_kendra.types.document_attribute_list.DocumentAttributeList"
    ]
    """<p>An array of document fields/attributes assigned to a document in the search results. For example, the document author (<code>_author</code>) or the source URI (<code>_source_uri</code>) of the document.</p>"""
    score_attributes: NotRequired[
        "aws_sdk_kendra.types.score_attributes.ScoreAttributes"
    ]
    """<p>The confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveResultItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "document_title" in value:
        out["DocumentTitle"] = value["document_title"]
    if "content" in value:
        out["Content"] = value["content"]
    if "document_uri" in value:
        out["DocumentURI"] = value["document_uri"]
    if "document_attributes" in value:
        import aws_sdk_kendra.types.document_attribute_list

        out["DocumentAttributes"] = (
            aws_sdk_kendra.types.document_attribute_list.serialize_aws_json_1_1(
                value["document_attributes"]
            )
        )
    if "score_attributes" in value:
        import aws_sdk_kendra.types.score_attributes

        out["ScoreAttributes"] = (
            aws_sdk_kendra.types.score_attributes.serialize_aws_json_1_1(
                value["score_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveResultItem:
    out: RetrieveResultItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "DocumentTitle" in data:
        out["document_title"] = data["DocumentTitle"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "DocumentURI" in data:
        out["document_uri"] = data["DocumentURI"]
    if "DocumentAttributes" in data:
        import aws_sdk_kendra.types.document_attribute_list

        out["document_attributes"] = (
            aws_sdk_kendra.types.document_attribute_list.deserialize_aws_json_1_1(
                data["DocumentAttributes"]
            )
        )
    if "ScoreAttributes" in data:
        import aws_sdk_kendra.types.score_attributes

        out["score_attributes"] = (
            aws_sdk_kendra.types.score_attributes.deserialize_aws_json_1_1(
                data["ScoreAttributes"]
            )
        )
    return out
