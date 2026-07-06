"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.custom_metadata_map
    import aws_sdk_workdocs.types.document_version_metadata


class GetDocumentVersionResponse(TypedDict, closed=True):
    metadata: NotRequired[
        "aws_sdk_workdocs.types.document_version_metadata.DocumentVersionMetadata"
    ]
    """<p>The version metadata.</p>"""
    custom_metadata: NotRequired[
        "aws_sdk_workdocs.types.custom_metadata_map.CustomMetadataMap"
    ]
    """<p>The custom metadata on the document version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentVersionResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_workdocs.types.document_version_metadata

        out["Metadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "custom_metadata" in value:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["CustomMetadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.serialize_json(
                value["custom_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDocumentVersionResponse:
    out: GetDocumentVersionResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_workdocs.types.document_version_metadata

        out["metadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.deserialize_json(
                data["Metadata"]
            )
        )
    if "CustomMetadata" in data:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    return out
