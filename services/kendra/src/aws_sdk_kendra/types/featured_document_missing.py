"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocumentMissing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_id


class FeaturedDocumentMissing(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.document_id.DocumentId"]
    """<p>The identifier of the document that doesn't exist but you have specified as a featured document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocumentMissing) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedDocumentMissing:
    out: FeaturedDocumentMissing = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
