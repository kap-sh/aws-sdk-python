"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeSnapshotsListMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.snapshot_list
    import aws_sdk_elasticache.types.string


class DescribeSnapshotsListMessage(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    snapshots: NotRequired["aws_sdk_elasticache.types.snapshot_list.SnapshotList"]
    """<p>A list of snapshots. Each item in the list contains detailed information about one snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSnapshotsListMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "snapshots" in value:
        import aws_sdk_elasticache.types.snapshot_list

        aws_sdk_elasticache.types.snapshot_list.serialize_query(
            value["snapshots"], pairs, f"{prefix}.Snapshots"
        )


def deserialize_query(el: Element) -> DescribeSnapshotsListMessage:
    out: DescribeSnapshotsListMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_snapshots = el.find("Snapshots")
    if child_snapshots is not None:
        import aws_sdk_elasticache.types.snapshot_list

        out["snapshots"] = aws_sdk_elasticache.types.snapshot_list.deserialize_query(
            child_snapshots
        )
    return out
