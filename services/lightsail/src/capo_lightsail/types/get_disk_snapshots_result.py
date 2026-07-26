"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.disk_snapshot_list
    import capo_lightsail.types.string


class GetDiskSnapshotsResult(TypedDict, closed=True):
    disk_snapshots: NotRequired[
        "capo_lightsail.types.disk_snapshot_list.DiskSnapshotList"
    ]
    """<p>An array of objects containing information about all block storage disk snapshots.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetDiskSnapshots</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskSnapshotsResult) -> dict:
    out: dict = {}
    if "disk_snapshots" in value:
        import capo_lightsail.types.disk_snapshot_list

        out["diskSnapshots"] = (
            capo_lightsail.types.disk_snapshot_list.serialize_aws_json_1_1(
                value["disk_snapshots"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskSnapshotsResult:
    out: GetDiskSnapshotsResult = {}  # type: ignore[typeddict-item]
    if "diskSnapshots" in data:
        import capo_lightsail.types.disk_snapshot_list

        out["disk_snapshots"] = (
            capo_lightsail.types.disk_snapshot_list.deserialize_aws_json_1_1(
                data["diskSnapshots"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
