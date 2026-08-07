"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeDBClusterSnapshotsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.filter_list
    import capo_neptune.types.integer_optional
    import capo_neptune.types.string


class DescribeDBClusterSnapshotsMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't be used in conjunction with the <code>DBClusterSnapshotIdentifier</code> parameter. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBCluster.</p> </li> </ul>"""
    db_cluster_snapshot_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>A specific DB cluster snapshot identifier to describe. This parameter can't be used in conjunction with the <code>DBClusterIdentifier</code> parameter. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBClusterSnapshot.</p> </li> <li> <p>If this identifier is for an automated snapshot, the <code>SnapshotType</code> parameter must also be specified.</p> </li> </ul>"""
    snapshot_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The type of DB cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my Amazon account.</p> </li> <li> <p> <code>manual</code> - Return all DB cluster snapshots that have been taken by my Amazon account.</p> </li> <li> <p> <code>shared</code> - Return all manual DB cluster snapshots that have been shared to my Amazon account.</p> </li> <li> <p> <code>public</code> - Return all DB cluster snapshots that have been marked as public.</p> </li> </ul> <p>If you don't specify a <code>SnapshotType</code> value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the <code>IncludeShared</code> parameter to <code>true</code>. You can include public DB cluster snapshots with these results by setting the <code>IncludePublic</code> parameter to <code>true</code>.</p> <p>The <code>IncludeShared</code> and <code>IncludePublic</code> parameters don't apply for <code>SnapshotType</code> values of <code>manual</code> or <code>automated</code>. The <code>IncludePublic</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>shared</code>. The <code>IncludeShared</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>public</code>.</p>"""
    filters: NotRequired["capo_neptune.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterSnapshots</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    include_shared: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>True to include shared manual DB cluster snapshots from other Amazon accounts that this Amazon account has been given permission to copy or restore, and otherwise false. The default is <code>false</code>.</p> <p>You can give an Amazon account permission to restore a manual DB cluster snapshot from another Amazon account by the <a>ModifyDBClusterSnapshotAttribute</a> API action.</p>"""
    include_public: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>True to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon account, and otherwise false. The default is <code>false</code>. The default is false.</p> <p>You can share a manual DB cluster snapshot as public by using the <a>ModifyDBClusterSnapshotAttribute</a> API action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterSnapshotsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "filters" in value:
        import capo_neptune.types.filter_list

        capo_neptune.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "include_shared" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeShared",
                "true" if value["include_shared"] else "false",
            )
        )
    if "include_public" in value:
        pairs.append(
            (
                f"{key_prefix}IncludePublic",
                "true" if value["include_public"] else "false",
            )
        )


def deserialize_query(el: Element) -> DescribeDBClusterSnapshotsMessage:
    out: DescribeDBClusterSnapshotsMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_neptune.types.filter_list

        out["filters"] = capo_neptune.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_include_shared = el.find("IncludeShared")
    if child_include_shared is not None:
        out["include_shared"] = (child_include_shared.text or "").lower() == "true"
    child_include_public = el.find("IncludePublic")
    if child_include_public is not None:
        out["include_public"] = (child_include_public.text or "").lower() == "true"
    return out
