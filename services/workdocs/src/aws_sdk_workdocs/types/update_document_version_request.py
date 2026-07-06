"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateDocumentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.document_version_id_type
    import aws_sdk_workdocs.types.document_version_status
    import aws_sdk_workdocs.types.resource_id_type


class UpdateDocumentVersionRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The version ID of the document.</p>"""
    version_status: NotRequired[
        "aws_sdk_workdocs.types.document_version_status.DocumentVersionStatus"
    ]
    """<p>The status of the version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDocumentVersionRequest) -> dict:
    out: dict = {}
    if "version_status" in value:
        import aws_sdk_workdocs.types.document_version_status

        out["VersionStatus"] = (
            aws_sdk_workdocs.types.document_version_status.serialize_json(
                value["version_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDocumentVersionRequest:
    out: UpdateDocumentVersionRequest = {}  # type: ignore[typeddict-item]
    if "VersionStatus" in data:
        import aws_sdk_workdocs.types.document_version_status

        out["version_status"] = (
            aws_sdk_workdocs.types.document_version_status.deserialize_json(
                data["VersionStatus"]
            )
        )
    return out
