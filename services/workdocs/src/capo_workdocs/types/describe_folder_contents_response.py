"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeFolderContentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_metadata_list
    import capo_workdocs.types.folder_metadata_list
    import capo_workdocs.types.page_marker_type


class DescribeFolderContentsResponse(TypedDict, closed=True):
    folders: NotRequired["capo_workdocs.types.folder_metadata_list.FolderMetadataList"]
    """<p>The subfolders in the specified folder.</p>"""
    documents: NotRequired[
        "capo_workdocs.types.document_metadata_list.DocumentMetadataList"
    ]
    """<p>The documents in the specified folder.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderContentsResponse) -> dict:
    out: dict = {}
    if "folders" in value:
        import capo_workdocs.types.folder_metadata_list

        out["Folders"] = capo_workdocs.types.folder_metadata_list.serialize_json(
            value["folders"]
        )
    if "documents" in value:
        import capo_workdocs.types.document_metadata_list

        out["Documents"] = capo_workdocs.types.document_metadata_list.serialize_json(
            value["documents"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeFolderContentsResponse:
    out: DescribeFolderContentsResponse = {}  # type: ignore[typeddict-item]
    if "Folders" in data:
        import capo_workdocs.types.folder_metadata_list

        out["folders"] = capo_workdocs.types.folder_metadata_list.deserialize_json(
            data["Folders"]
        )
    if "Documents" in data:
        import capo_workdocs.types.document_metadata_list

        out["documents"] = capo_workdocs.types.document_metadata_list.deserialize_json(
            data["Documents"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
