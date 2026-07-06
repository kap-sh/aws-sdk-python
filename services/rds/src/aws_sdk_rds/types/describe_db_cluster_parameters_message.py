"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBClusterParametersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBClusterParametersMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of a specific DB cluster parameter group to return parameter details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>"""
    source: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A specific source to return parameters for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>engine-default</code> </p> </li> <li> <p> <code>system</code> </p> </li> <li> <p> <code>user</code> </p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB cluster parameters to describe.</p> <p>The only supported filter is <code>parameter-name</code>. The results list only includes information about the DB cluster parameters with these names.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterParametersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBClusterParametersMessage:
    out: DescribeDBClusterParametersMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
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
