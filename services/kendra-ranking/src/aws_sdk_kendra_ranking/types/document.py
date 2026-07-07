"""Generated from Smithy shape ``com.amazonaws.kendraranking#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.body_tokens_list
    import aws_sdk_kendra_ranking.types.document_body
    import aws_sdk_kendra_ranking.types.document_id
    import aws_sdk_kendra_ranking.types.document_title
    import aws_sdk_kendra_ranking.types.float
    import aws_sdk_kendra_ranking.types.group_id
    import aws_sdk_kendra_ranking.types.title_tokens_list


class Document(TypedDict, closed=True):
    id: "aws_sdk_kendra_ranking.types.document_id.DocumentId"
    """<p>The identifier of the document from the search service.</p>"""
    group_id: NotRequired["aws_sdk_kendra_ranking.types.group_id.GroupId"]
    """<p>The optional group identifier of the document from the search service. Documents with the same group identifier are grouped together and processed as one document within the service.</p>"""
    title: NotRequired["aws_sdk_kendra_ranking.types.document_title.DocumentTitle"]
    """<p>The title of the search service's document.</p>"""
    body: NotRequired["aws_sdk_kendra_ranking.types.document_body.DocumentBody"]
    """<p>The body text of the search service's document.</p>"""
    tokenized_title: NotRequired[
        "aws_sdk_kendra_ranking.types.title_tokens_list.TitleTokensList"
    ]
    """<p>The title of the search service's document represented as a list of tokens or words. You must choose to provide <code>Title</code> or <code>TokenizedTitle</code>. You cannot provide both.</p>"""
    tokenized_body: NotRequired[
        "aws_sdk_kendra_ranking.types.body_tokens_list.BodyTokensList"
    ]
    """<p>The body text of the search service's document represented as a list of tokens or words. You must choose to provide <code>Body</code> or <code>TokenizedBody</code>. You cannot provide both.</p>"""
    original_score: "aws_sdk_kendra_ranking.types.float.Float"
    """<p>The original document score or rank from the search service. Amazon Kendra Intelligent Ranking gives the document a new score or rank based on its intelligent search algorithms.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Document) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "body" in value:
        out["Body"] = value["body"]
    if "tokenized_title" in value:
        import aws_sdk_kendra_ranking.types.title_tokens_list

        out["TokenizedTitle"] = (
            aws_sdk_kendra_ranking.types.title_tokens_list.serialize_aws_json_1_0(
                value["tokenized_title"]
            )
        )
    if "tokenized_body" in value:
        import aws_sdk_kendra_ranking.types.body_tokens_list

        out["TokenizedBody"] = (
            aws_sdk_kendra_ranking.types.body_tokens_list.serialize_aws_json_1_0(
                value["tokenized_body"]
            )
        )
    out["OriginalScore"] = value["original_score"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Document.id required")
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Body" in data:
        out["body"] = data["Body"]
    if "TokenizedTitle" in data:
        import aws_sdk_kendra_ranking.types.title_tokens_list

        out["tokenized_title"] = (
            aws_sdk_kendra_ranking.types.title_tokens_list.deserialize_aws_json_1_0(
                data["TokenizedTitle"]
            )
        )
    if "TokenizedBody" in data:
        import aws_sdk_kendra_ranking.types.body_tokens_list

        out["tokenized_body"] = (
            aws_sdk_kendra_ranking.types.body_tokens_list.deserialize_aws_json_1_0(
                data["TokenizedBody"]
            )
        )
    if "OriginalScore" in data:
        out["original_score"] = data["OriginalScore"]
    else:
        raise DeserializationError("Document.original_score required")
    return out
