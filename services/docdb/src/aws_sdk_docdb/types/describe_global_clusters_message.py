"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeGlobalClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.filter_list
    import aws_sdk_docdb.types.global_cluster_identifier
    import aws_sdk_docdb.types.integer_optional
    import aws_sdk_docdb.types.string


class DescribeGlobalClustersMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The user-supplied cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case-sensitive.</p>"""
    filters: NotRequired["aws_sdk_docdb.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more global DB clusters to describe.</p> <p>Supported filters: <code>db-cluster-id</code> accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list will only include information about the clusters identified by these ARNs.</p>"""
    max_records: NotRequired["aws_sdk_docdb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results. </p>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeGlobalClusters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGlobalClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "filters" in value:
        import aws_sdk_docdb.types.filter_list

        aws_sdk_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeGlobalClustersMessage:
    out: DescribeGlobalClustersMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_docdb.types.filter_list

        out["filters"] = aws_sdk_docdb.types.filter_list.deserialize_query(
            child_filters
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
