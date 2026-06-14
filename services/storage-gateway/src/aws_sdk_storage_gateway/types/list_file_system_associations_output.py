"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListFileSystemAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_summary_list
    import aws_sdk_storage_gateway.types.marker


class ListFileSystemAssociationsOutput(TypedDict):
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>If the request includes <code>Marker</code>, the response returns that value in this field.</p>"""
    next_marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>If a value is present, there are more file system associations to return. In a subsequent request, use <code>NextMarker</code> as the value for <code>Marker</code> to retrieve the next set of file system associations.</p>"""
    file_system_association_summary_list: NotRequired[
        "aws_sdk_storage_gateway.types.file_system_association_summary_list.FileSystemAssociationSummaryList"
    ]
    """<p>An array of information about the Amazon FSx gateway's file system associations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileSystemAssociationsOutput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "file_system_association_summary_list" in value:
        import aws_sdk_storage_gateway.types.file_system_association_summary_list

        out["FileSystemAssociationSummaryList"] = (
            aws_sdk_storage_gateway.types.file_system_association_summary_list.serialize_aws_json_1_1(
                value["file_system_association_summary_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileSystemAssociationsOutput:
    out: ListFileSystemAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "FileSystemAssociationSummaryList" in data:
        import aws_sdk_storage_gateway.types.file_system_association_summary_list

        out["file_system_association_summary_list"] = (
            aws_sdk_storage_gateway.types.file_system_association_summary_list.deserialize_aws_json_1_1(
                data["FileSystemAssociationSummaryList"]
            )
        )
    return out
