"""Generated from Smithy shape ``com.amazonaws.kendra#GetSnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.next_token
    import capo_kendra.types.snapshots_data_header_fields
    import capo_kendra.types.snapshots_data_records
    import capo_kendra.types.time_range


class GetSnapshotsResponse(TypedDict, closed=True):
    snap_shot_time_filter: NotRequired["capo_kendra.types.time_range.TimeRange"]
    """<p>The Unix timestamp for the beginning and end of the time window for the search metrics data.</p>"""
    snapshots_data_header: NotRequired[
        "capo_kendra.types.snapshots_data_header_fields.SnapshotsDataHeaderFields"
    ]
    """<p>The column headers for the search metrics data.</p>"""
    snapshots_data: NotRequired[
        "capo_kendra.types.snapshots_data_records.SnapshotsDataRecords"
    ]
    """<p>The search metrics data. The data returned depends on the metric type you requested.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token, which you can use in a later request to retrieve the next set of search metrics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnapshotsResponse) -> dict:
    out: dict = {}
    if "snap_shot_time_filter" in value:
        import capo_kendra.types.time_range

        out["SnapShotTimeFilter"] = capo_kendra.types.time_range.serialize_aws_json_1_1(
            value["snap_shot_time_filter"]
        )
    if "snapshots_data_header" in value:
        import capo_kendra.types.snapshots_data_header_fields

        out["SnapshotsDataHeader"] = (
            capo_kendra.types.snapshots_data_header_fields.serialize_aws_json_1_1(
                value["snapshots_data_header"]
            )
        )
    if "snapshots_data" in value:
        import capo_kendra.types.snapshots_data_records

        out["SnapshotsData"] = (
            capo_kendra.types.snapshots_data_records.serialize_aws_json_1_1(
                value["snapshots_data"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnapshotsResponse:
    out: GetSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "SnapShotTimeFilter" in data:
        import capo_kendra.types.time_range

        out["snap_shot_time_filter"] = (
            capo_kendra.types.time_range.deserialize_aws_json_1_1(
                data["SnapShotTimeFilter"]
            )
        )
    if "SnapshotsDataHeader" in data:
        import capo_kendra.types.snapshots_data_header_fields

        out["snapshots_data_header"] = (
            capo_kendra.types.snapshots_data_header_fields.deserialize_aws_json_1_1(
                data["SnapshotsDataHeader"]
            )
        )
    if "SnapshotsData" in data:
        import capo_kendra.types.snapshots_data_records

        out["snapshots_data"] = (
            capo_kendra.types.snapshots_data_records.deserialize_aws_json_1_1(
                data["SnapshotsData"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
