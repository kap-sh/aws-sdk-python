"""Generated from Smithy shape ``com.amazonaws.quicksight#UploadedDocumentMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.uploaded_document_name


class UploadedDocumentMetadata(TypedDict):
    name: NotRequired[
        "aws_sdk_quicksight.types.uploaded_document_name.UploadedDocumentName"
    ]
    """<p>The name of the uploaded document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadedDocumentMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UploadedDocumentMetadata:
    out: UploadedDocumentMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
