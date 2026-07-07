"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_cluster_snapshot_list
    import aws_sdk_neptune.types.string


class DBClusterSnapshotMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous <a>DescribeDBClusterSnapshots</a> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    db_cluster_snapshots: NotRequired[
        "aws_sdk_neptune.types.db_cluster_snapshot_list.DBClusterSnapshotList"
    ]
    """<p>Provides a list of DB cluster snapshots for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_cluster_snapshots" in value:
        import aws_sdk_neptune.types.db_cluster_snapshot_list

        aws_sdk_neptune.types.db_cluster_snapshot_list.serialize_query(
            value["db_cluster_snapshots"], pairs, f"{prefix}.DBClusterSnapshots"
        )


def deserialize_query(el: Element) -> DBClusterSnapshotMessage:
    out: DBClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_snapshots = el.find("DBClusterSnapshots")
    if child_db_cluster_snapshots is not None:
        import aws_sdk_neptune.types.db_cluster_snapshot_list

        out["db_cluster_snapshots"] = (
            aws_sdk_neptune.types.db_cluster_snapshot_list.deserialize_query(
                child_db_cluster_snapshots
            )
        )
    return out
