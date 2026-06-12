"""Generated from Smithy shape ``com.amazonaws.workdocs#GetResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_metadata_list
    import aws_sdk_workdocs.types.folder_metadata_list
    import aws_sdk_workdocs.types.page_marker_type


class GetResourcesResponse(TypedDict):
    folders: NotRequired[
        "aws_sdk_workdocs.types.folder_metadata_list.FolderMetadataList"
    ]
    """<p>The folders in the specified folder.</p>"""
    documents: NotRequired[
        "aws_sdk_workdocs.types.document_metadata_list.DocumentMetadataList"
    ]
    """<p>The documents in the specified collection.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesResponse) -> dict:
    out: dict = {}
    if "folders" in value:
        import aws_sdk_workdocs.types.folder_metadata_list

        out["Folders"] = aws_sdk_workdocs.types.folder_metadata_list.serialize_json(
            value["folders"]
        )
    if "documents" in value:
        import aws_sdk_workdocs.types.document_metadata_list

        out["Documents"] = aws_sdk_workdocs.types.document_metadata_list.serialize_json(
            value["documents"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> GetResourcesResponse:
    out: GetResourcesResponse = {}  # type: ignore[typeddict-item]
    if "Folders" in data:
        import aws_sdk_workdocs.types.folder_metadata_list

        out["folders"] = aws_sdk_workdocs.types.folder_metadata_list.deserialize_json(
            data["Folders"]
        )
    if "Documents" in data:
        import aws_sdk_workdocs.types.document_metadata_list

        out["documents"] = (
            aws_sdk_workdocs.types.document_metadata_list.deserialize_json(
                data["Documents"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
