"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocumentWithMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_id
    import aws_sdk_kendra.types.string
    import aws_sdk_kendra.types.url


class FeaturedDocumentWithMetadata(TypedDict):
    id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the featured document with its metadata. You can use the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html\">Query</a> API to search for specific documents with their document IDs included in the result items, or you can use the console.</p>"""
    title: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>The main title of the featured document.</p>"""
    uri: NotRequired["aws_sdk_kendra.types.url.Url"]
    """<p>The source URI location of the featured document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocumentWithMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "uri" in value:
        out["URI"] = value["uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedDocumentWithMetadata:
    out: FeaturedDocumentWithMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "URI" in data:
        out["uri"] = data["URI"]
    return out
