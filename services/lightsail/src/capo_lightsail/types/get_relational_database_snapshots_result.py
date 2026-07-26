"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_snapshot_list
    import capo_lightsail.types.string


class GetRelationalDatabaseSnapshotsResult(TypedDict, closed=True):
    relational_database_snapshots: NotRequired[
        "capo_lightsail.types.relational_database_snapshot_list.RelationalDatabaseSnapshotList"
    ]
    """<p>An object describing the result of your get relational database snapshots request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabaseSnapshots</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseSnapshotsResult) -> dict:
    out: dict = {}
    if "relational_database_snapshots" in value:
        import capo_lightsail.types.relational_database_snapshot_list

        out["relationalDatabaseSnapshots"] = (
            capo_lightsail.types.relational_database_snapshot_list.serialize_aws_json_1_1(
                value["relational_database_snapshots"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseSnapshotsResult:
    out: GetRelationalDatabaseSnapshotsResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseSnapshots" in data:
        import capo_lightsail.types.relational_database_snapshot_list

        out["relational_database_snapshots"] = (
            capo_lightsail.types.relational_database_snapshot_list.deserialize_aws_json_1_1(
                data["relationalDatabaseSnapshots"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
