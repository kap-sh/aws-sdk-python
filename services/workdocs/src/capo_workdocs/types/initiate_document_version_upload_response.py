"""Generated from Smithy shape ``com.amazonaws.workdocs#InitiateDocumentVersionUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_metadata
    import capo_workdocs.types.upload_metadata


class InitiateDocumentVersionUploadResponse(TypedDict, closed=True):
    metadata: NotRequired["capo_workdocs.types.document_metadata.DocumentMetadata"]
    """<p>The document metadata.</p>"""
    upload_metadata: NotRequired["capo_workdocs.types.upload_metadata.UploadMetadata"]
    """<p>The upload metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateDocumentVersionUploadResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_workdocs.types.document_metadata

        out["Metadata"] = capo_workdocs.types.document_metadata.serialize_json(
            value["metadata"]
        )
    if "upload_metadata" in value:
        import capo_workdocs.types.upload_metadata

        out["UploadMetadata"] = capo_workdocs.types.upload_metadata.serialize_json(
            value["upload_metadata"]
        )
    return out


def deserialize_json(data: dict) -> InitiateDocumentVersionUploadResponse:
    out: InitiateDocumentVersionUploadResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import capo_workdocs.types.document_metadata

        out["metadata"] = capo_workdocs.types.document_metadata.deserialize_json(
            data["Metadata"]
        )
    if "UploadMetadata" in data:
        import capo_workdocs.types.upload_metadata

        out["upload_metadata"] = capo_workdocs.types.upload_metadata.deserialize_json(
            data["UploadMetadata"]
        )
    return out
