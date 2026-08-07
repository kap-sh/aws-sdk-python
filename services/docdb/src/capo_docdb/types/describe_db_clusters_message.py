"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeDBClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.filter_list
    import capo_docdb.types.integer_optional
    import capo_docdb.types.string


class DescribeDBClustersMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match an existing <code>DBClusterIdentifier</code>.</p> </li> </ul>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more clusters to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.</p> </li> </ul>"""
    max_records: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "filters" in value:
        import capo_docdb.types.filter_list

        capo_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBClustersMessage:
    out: DescribeDBClustersMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_docdb.types.filter_list

        out["filters"] = capo_docdb.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
