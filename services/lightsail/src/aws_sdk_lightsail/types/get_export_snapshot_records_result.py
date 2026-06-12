"""Generated from Smithy shape ``com.amazonaws.lightsail#GetExportSnapshotRecordsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.export_snapshot_record_list
    import aws_sdk_lightsail.types.string


class GetExportSnapshotRecordsResult(TypedDict):
    export_snapshot_records: NotRequired[
        "aws_sdk_lightsail.types.export_snapshot_record_list.ExportSnapshotRecordList"
    ]
    """<p>A list of objects describing the export snapshot records.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetExportSnapshotRecords</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportSnapshotRecordsResult) -> dict:
    out: dict = {}
    if "export_snapshot_records" in value:
        import aws_sdk_lightsail.types.export_snapshot_record_list

        out["exportSnapshotRecords"] = (
            aws_sdk_lightsail.types.export_snapshot_record_list.serialize_aws_json_1_1(
                value["export_snapshot_records"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportSnapshotRecordsResult:
    out: GetExportSnapshotRecordsResult = {}  # type: ignore[typeddict-item]
    if "exportSnapshotRecords" in data:
        import aws_sdk_lightsail.types.export_snapshot_record_list

        out["export_snapshot_records"] = (
            aws_sdk_lightsail.types.export_snapshot_record_list.deserialize_aws_json_1_1(
                data["exportSnapshotRecords"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
