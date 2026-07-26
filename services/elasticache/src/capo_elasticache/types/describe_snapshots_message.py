"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeSnapshotsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.string


class DescribeSnapshotsMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.</p>"""
    snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.</p>"""
    snapshot_source: NotRequired["capo_elasticache.types.string.String"]
    """<p>If set to <code>system</code>, the output shows snapshots that were automatically created by ElastiCache. If set to <code>user</code> the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.</p>"""
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 50</p> <p>Constraints: minimum 20; maximum 50.</p>"""
    show_node_group_config: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSnapshotsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "snapshot_name" in value:
        pairs.append((f"{prefix}.SnapshotName", str(value["snapshot_name"])))
    if "snapshot_source" in value:
        pairs.append((f"{prefix}.SnapshotSource", str(value["snapshot_source"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "show_node_group_config" in value:
        pairs.append(
            (
                f"{prefix}.ShowNodeGroupConfig",
                "true" if value["show_node_group_config"] else "false",
            )
        )


def deserialize_query(el: Element) -> DescribeSnapshotsMessage:
    out: DescribeSnapshotsMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_snapshot_name = el.find("SnapshotName")
    if child_snapshot_name is not None:
        out["snapshot_name"] = str(child_snapshot_name.text or "")
    child_snapshot_source = el.find("SnapshotSource")
    if child_snapshot_source is not None:
        out["snapshot_source"] = str(child_snapshot_source.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_show_node_group_config = el.find("ShowNodeGroupConfig")
    if child_show_node_group_config is not None:
        out["show_node_group_config"] = (
            child_show_node_group_config.text or ""
        ).lower() == "true"
    return out
