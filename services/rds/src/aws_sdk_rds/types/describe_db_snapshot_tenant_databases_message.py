"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBSnapshotTenantDatabasesMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBSnapshotTenantDatabasesMessage(TypedDict):
    db_instance_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The ID of the DB instance used to create the DB snapshots. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>"""
    db_snapshot_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The ID of a DB snapshot that contains the tenant databases to describe. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>If you specify this parameter, the value must match the ID of an existing DB snapshot.</p> </li> <li> <p>If you specify an automatic snapshot, you must also specify <code>SnapshotType</code>.</p> </li> </ul>"""
    snapshot_type: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The type of DB snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> – All DB snapshots that have been automatically taken by Amazon RDS for my Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> – All DB snapshots that have been taken by my Amazon Web Services account.</p> </li> <li> <p> <code>shared</code> – All manual DB snapshots that have been shared to my Amazon Web Services account.</p> </li> <li> <p> <code>public</code> – All DB snapshots that have been marked as public.</p> </li> <li> <p> <code>awsbackup</code> – All DB snapshots managed by the Amazon Web Services Backup service.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more tenant databases to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>tenant-db-name</code> - Tenant database names. The results list only includes information about the tenant databases that match these tenant DB names.</p> </li> <li> <p> <code>tenant-database-resource-id</code> - Tenant database resource identifiers. The results list only includes information about the tenant databases contained within the DB snapshots.</p> </li> <li> <p> <code>dbi-resource-id</code> - DB instance resource identifiers. The results list only includes information about snapshots containing tenant databases contained within the DB instances identified by these resource identifiers.</p> </li> <li> <p> <code>db-instance-id</code> - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).</p> </li> <li> <p> <code>db-snapshot-id</code> - Accepts DB snapshot identifiers.</p> </li> <li> <p> <code>snapshot-type</code> - Accepts types of DB snapshots.</p> </li> </ul>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBSnapshotTenantDatabases</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    dbi_resource_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A specific DB resource identifier to describe.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBSnapshotTenantDatabasesMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "snapshot_type" in value:
        pairs.append((f"{prefix}.SnapshotType", str(value["snapshot_type"])))
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{prefix}.DbiResourceId", str(value["dbi_resource_id"])))


def deserialize_query(el: Element) -> DescribeDBSnapshotTenantDatabasesMessage:
    out: DescribeDBSnapshotTenantDatabasesMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_rds.types.filter_list

        out["filters"] = aws_sdk_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    return out
