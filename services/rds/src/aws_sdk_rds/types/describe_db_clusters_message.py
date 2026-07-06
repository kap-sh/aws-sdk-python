"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBClustersMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The user-supplied DB cluster identifier or the Amazon Resource Name (ARN) of the DB cluster. If this parameter is specified, information for only the specific DB cluster is returned. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DB cluster identifier.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB clusters to describe.</p> <p>Supported Filters:</p> <ul> <li> <p> <code>clone-group-id</code> - Accepts clone group identifiers. The results list only includes information about the DB clusters associated with these clone groups.</p> </li> <li> <p> <code>db-cluster-id</code> - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list only includes information about the DB clusters identified by these ARNs.</p> </li> <li> <p> <code>db-cluster-resource-id</code> - Accepts DB cluster resource identifiers. The results list will only include information about the DB clusters identified by these DB cluster resource identifiers.</p> </li> <li> <p> <code>domain</code> - Accepts Active Directory directory IDs. The results list only includes information about the DB clusters associated with these domains.</p> </li> <li> <p> <code>engine</code> - Accepts engine names. The results list only includes information about the DB clusters for these engines.</p> </li> </ul>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    include_shared: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether the output includes information about clusters shared from other Amazon Web Services accounts.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
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
    if "include_shared" in value:
        pairs.append(
            (f"{prefix}.IncludeShared", "true" if value["include_shared"] else "false")
        )


def deserialize_query(el: Element) -> DescribeDBClustersMessage:
    out: DescribeDBClustersMessage = {}  # type: ignore[typeddict-item]
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
    child_include_shared = el.find("IncludeShared")
    if child_include_shared is not None:
        out["include_shared"] = (child_include_shared.text or "").lower() == "true"
    return out
