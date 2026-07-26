"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListClusterSnapshotsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_snapshot_list
    import capo_docdb_elastic.types.pagination_token


class ListClusterSnapshotsOutput(TypedDict, closed=True):
    snapshots: NotRequired[
        "capo_docdb_elastic.types.cluster_snapshot_list.ClusterSnapshotList"
    ]
    """<p>A list of snapshots for a specified elastic cluster.</p>"""
    next_token: NotRequired["capo_docdb_elastic.types.pagination_token.PaginationToken"]
    """<p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterSnapshotsOutput) -> dict:
    out: dict = {}
    if "snapshots" in value:
        import capo_docdb_elastic.types.cluster_snapshot_list

        out["snapshots"] = (
            capo_docdb_elastic.types.cluster_snapshot_list.serialize_json(
                value["snapshots"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClusterSnapshotsOutput:
    out: ListClusterSnapshotsOutput = {}  # type: ignore[typeddict-item]
    if "snapshots" in data:
        import capo_docdb_elastic.types.cluster_snapshot_list

        out["snapshots"] = (
            capo_docdb_elastic.types.cluster_snapshot_list.deserialize_json(
                data["snapshots"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
