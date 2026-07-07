"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBClusterAutomatedBackupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBClusterAutomatedBackupsMessage(TypedDict, closed=True):
    db_cluster_resource_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The resource ID of the DB cluster that is the source of the automated backup. This parameter isn't case-sensitive.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>(Optional) The user-supplied DB cluster identifier. If this parameter is specified, it must match the identifier of an existing DB cluster. It returns information from the specific DB cluster's automated backup. This parameter isn't case-sensitive.</p>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies which resources to return based on status.</p> <p>Supported filters are the following:</p> <ul> <li> <p> <code>status</code> </p> <ul> <li> <p> <code>retained</code> - Automated backups for deleted clusters and after backup replication is stopped.</p> </li> </ul> </li> <li> <p> <code>db-cluster-id</code> - Accepts DB cluster identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB cluster automated backups identified by these ARNs.</p> </li> <li> <p> <code>db-cluster-resource-id</code> - Accepts DB resource identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB cluster resources identified by these ARNs.</p> </li> </ul> <p>Returns all resources by default. The status for each resource is specified in the response.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterAutomatedBackupsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_resource_id" in value:
        pairs.append(
            (f"{prefix}.DbClusterResourceId", str(value["db_cluster_resource_id"]))
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
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


def deserialize_query(el: Element) -> DescribeDBClusterAutomatedBackupsMessage:
    out: DescribeDBClusterAutomatedBackupsMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_resource_id = el.find("DbClusterResourceId")
    if child_db_cluster_resource_id is not None:
        out["db_cluster_resource_id"] = str(child_db_cluster_resource_id.text or "")
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
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
    return out
