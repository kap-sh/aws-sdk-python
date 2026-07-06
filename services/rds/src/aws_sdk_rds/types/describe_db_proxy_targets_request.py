"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxyTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_name
    import aws_sdk_rds.types.db_proxy_target_group_name
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.max_records
    import aws_sdk_rds.types.string


class DescribeDBProxyTargetsRequest(TypedDict, closed=True):
    db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The identifier of the <code>DBProxyTarget</code> to describe.</p>"""
    target_group_name: NotRequired[
        "aws_sdk_rds.types.db_proxy_target_group_name.DBProxyTargetGroupName"
    ]
    """<p>The identifier of the <code>DBProxyTargetGroup</code> to describe.</p>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxyTargetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))
    if "target_group_name" in value:
        pairs.append((f"{prefix}.TargetGroupName", str(value["target_group_name"])))
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeDBProxyTargetsRequest:
    out: DescribeDBProxyTargetsRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_target_group_name = el.find("TargetGroupName")
    if child_target_group_name is not None:
        out["target_group_name"] = str(child_target_group_name.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_rds.types.filter_list

        out["filters"] = aws_sdk_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
