"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListFileSharesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_share_info_list
    import aws_sdk_storage_gateway.types.marker


class ListFileSharesOutput(TypedDict):
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>If the request includes <code>Marker</code>, the response returns that value in this field.</p>"""
    next_marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>If a value is present, there are more file shares to return. In a subsequent request, use <code>NextMarker</code> as the value for <code>Marker</code> to retrieve the next set of file shares.</p>"""
    file_share_info_list: NotRequired[
        "aws_sdk_storage_gateway.types.file_share_info_list.FileShareInfoList"
    ]
    """<p>An array of information about the S3 File Gateway's file shares.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileSharesOutput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "file_share_info_list" in value:
        import aws_sdk_storage_gateway.types.file_share_info_list

        out["FileShareInfoList"] = (
            aws_sdk_storage_gateway.types.file_share_info_list.serialize_aws_json_1_1(
                value["file_share_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileSharesOutput:
    out: ListFileSharesOutput = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "FileShareInfoList" in data:
        import aws_sdk_storage_gateway.types.file_share_info_list

        out["file_share_info_list"] = (
            aws_sdk_storage_gateway.types.file_share_info_list.deserialize_aws_json_1_1(
                data["FileShareInfoList"]
            )
        )
    return out
