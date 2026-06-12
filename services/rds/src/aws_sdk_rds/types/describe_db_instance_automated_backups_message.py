"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBInstanceAutomatedBackupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBInstanceAutomatedBackupsMessage(TypedDict):
    dbi_resource_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The resource ID of the DB instance that is the source of the automated backup. This parameter isn't case-sensitive.</p>"""
    db_instance_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>(Optional) The user-supplied instance identifier. If this parameter is specified, it must match the identifier of an existing DB instance. It returns information from the specific DB instance's automated backup. This parameter isn't case-sensitive.</p>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies which resources to return based on status.</p> <p>Supported filters are the following:</p> <ul> <li> <p> <code>status</code> </p> <ul> <li> <p> <code>active</code> - Automated backups for current instances.</p> </li> <li> <p> <code>creating</code> - Automated backups that are waiting for the first automated snapshot to be available.</p> </li> <li> <p> <code>retained</code> - Automated backups for deleted instances and after backup replication is stopped.</p> </li> </ul> </li> <li> <p> <code>db-instance-id</code> - Accepts DB instance identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance automated backups identified by these ARNs.</p> </li> <li> <p> <code>dbi-resource-id</code> - Accepts DB resource identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance resources identified by these ARNs.</p> </li> </ul> <p>Returns all resources by default. The status for each resource is specified in the response.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to <code>MaxRecords</code>.</p>"""
    db_instance_automated_backups_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the replicated automated backups, for example, <code>arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE</code>.</p> <p>This setting doesn't apply to RDS Custom.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBInstanceAutomatedBackupsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dbi_resource_id" in value:
        pairs.append((f"{prefix}.DbiResourceId", str(value["dbi_resource_id"])))
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_instance_automated_backups_arn" in value:
        pairs.append(
            (
                f"{prefix}.DBInstanceAutomatedBackupsArn",
                str(value["db_instance_automated_backups_arn"]),
            )
        )


def deserialize_query(el: Element) -> DescribeDBInstanceAutomatedBackupsMessage:
    out: DescribeDBInstanceAutomatedBackupsMessage = {}  # type: ignore[typeddict-item]
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
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
    child_db_instance_automated_backups_arn = el.find("DBInstanceAutomatedBackupsArn")
    if child_db_instance_automated_backups_arn is not None:
        out["db_instance_automated_backups_arn"] = str(
            child_db_instance_automated_backups_arn.text or ""
        )
    return out
