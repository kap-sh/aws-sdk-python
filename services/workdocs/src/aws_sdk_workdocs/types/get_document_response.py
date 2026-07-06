"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.custom_metadata_map
    import aws_sdk_workdocs.types.document_metadata


class GetDocumentResponse(TypedDict, closed=True):
    metadata: NotRequired["aws_sdk_workdocs.types.document_metadata.DocumentMetadata"]
    """<p>The metadata details of the document.</p>"""
    custom_metadata: NotRequired[
        "aws_sdk_workdocs.types.custom_metadata_map.CustomMetadataMap"
    ]
    """<p>The custom metadata on the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_workdocs.types.document_metadata

        out["Metadata"] = aws_sdk_workdocs.types.document_metadata.serialize_json(
            value["metadata"]
        )
    if "custom_metadata" in value:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["CustomMetadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.serialize_json(
                value["custom_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDocumentResponse:
    out: GetDocumentResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_workdocs.types.document_metadata

        out["metadata"] = aws_sdk_workdocs.types.document_metadata.deserialize_json(
            data["Metadata"]
        )
    if "CustomMetadata" in data:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    return out
