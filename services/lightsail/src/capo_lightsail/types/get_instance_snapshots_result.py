"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_snapshot_list
    import capo_lightsail.types.string


class GetInstanceSnapshotsResult(TypedDict, closed=True):
    instance_snapshots: NotRequired[
        "capo_lightsail.types.instance_snapshot_list.InstanceSnapshotList"
    ]
    """<p>An array of key-value pairs containing information about the results of your get instance snapshots request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetInstanceSnapshots</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceSnapshotsResult) -> dict:
    out: dict = {}
    if "instance_snapshots" in value:
        import capo_lightsail.types.instance_snapshot_list

        out["instanceSnapshots"] = (
            capo_lightsail.types.instance_snapshot_list.serialize_aws_json_1_1(
                value["instance_snapshots"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceSnapshotsResult:
    out: GetInstanceSnapshotsResult = {}  # type: ignore[typeddict-item]
    if "instanceSnapshots" in data:
        import capo_lightsail.types.instance_snapshot_list

        out["instance_snapshots"] = (
            capo_lightsail.types.instance_snapshot_list.deserialize_aws_json_1_1(
                data["instanceSnapshots"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
