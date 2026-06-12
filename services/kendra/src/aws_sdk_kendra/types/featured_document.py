"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_id


class FeaturedDocument(TypedDict):
    id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document to feature in the search results. You can use the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html\">Query</a> API to search for specific documents with their document IDs included in the result items, or you can use the console.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocument) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedDocument:
    out: FeaturedDocument = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
