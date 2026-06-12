"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#UploadDocumentsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.adds
    import aws_sdk_cloudsearch_domain.types.deletes
    import aws_sdk_cloudsearch_domain.types.document_service_warnings
    import aws_sdk_cloudsearch_domain.types.string


class UploadDocumentsResponse(TypedDict):
    status: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The status of an <code>UploadDocumentsRequest</code>.</p>"""
    adds: "aws_sdk_cloudsearch_domain.types.adds.Adds"
    """<p>The number of documents that were added to the search domain.</p>"""
    deletes: "aws_sdk_cloudsearch_domain.types.deletes.Deletes"
    """<p>The number of documents that were deleted from the search domain.</p>"""
    warnings: NotRequired[
        "aws_sdk_cloudsearch_domain.types.document_service_warnings.DocumentServiceWarnings"
    ]
    """<p>Any warnings returned by the document service about the documents being uploaded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadDocumentsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    out["adds"] = value.get("adds", 0)
    out["deletes"] = value.get("deletes", 0)
    if "warnings" in value:
        import aws_sdk_cloudsearch_domain.types.document_service_warnings

        out["warnings"] = (
            aws_sdk_cloudsearch_domain.types.document_service_warnings.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UploadDocumentsResponse:
    out: UploadDocumentsResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "adds" in data:
        out["adds"] = data["adds"]
    else:
        out["adds"] = 0
    if "deletes" in data:
        out["deletes"] = data["deletes"]
    else:
        out["deletes"] = 0
    if "warnings" in data:
        import aws_sdk_cloudsearch_domain.types.document_service_warnings

        out["warnings"] = (
            aws_sdk_cloudsearch_domain.types.document_service_warnings.deserialize_json(
                data["warnings"]
            )
        )
    return out
