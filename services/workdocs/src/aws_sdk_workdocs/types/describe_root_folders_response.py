"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeRootFoldersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.folder_metadata_list
    import aws_sdk_workdocs.types.page_marker_type


class DescribeRootFoldersResponse(TypedDict):
    folders: NotRequired[
        "aws_sdk_workdocs.types.folder_metadata_list.FolderMetadataList"
    ]
    """<p>The user's special folders.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRootFoldersResponse) -> dict:
    out: dict = {}
    if "folders" in value:
        import aws_sdk_workdocs.types.folder_metadata_list

        out["Folders"] = aws_sdk_workdocs.types.folder_metadata_list.serialize_json(
            value["folders"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeRootFoldersResponse:
    out: DescribeRootFoldersResponse = {}  # type: ignore[typeddict-item]
    if "Folders" in data:
        import aws_sdk_workdocs.types.folder_metadata_list

        out["folders"] = aws_sdk_workdocs.types.folder_metadata_list.deserialize_json(
            data["Folders"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
