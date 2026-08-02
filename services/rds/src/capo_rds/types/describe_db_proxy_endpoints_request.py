"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxyEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_endpoint_name
    import capo_rds.types.db_proxy_name
    import capo_rds.types.filter_list
    import capo_rds.types.max_records
    import capo_rds.types.string


class DescribeDBProxyEndpointsRequest(TypedDict, closed=True):
    db_proxy_name: NotRequired["capo_rds.types.db_proxy_name.DBProxyName"]
    """<p>The name of the DB proxy whose endpoints you want to describe. If you omit this parameter, the output includes information about all DB proxy endpoints associated with all your DB proxies.</p>"""
    db_proxy_endpoint_name: NotRequired[
        "capo_rds.types.db_proxy_endpoint_name.DBProxyEndpointName"
    ]
    """<p>The name of a DB proxy endpoint to describe. If you omit this parameter, the output includes information about all DB proxy endpoints associated with the specified proxy.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxyEndpointsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_name" in value:
        pairs.append((f"{key_prefix}DBProxyName", str(value["db_proxy_name"])))
    if "db_proxy_endpoint_name" in value:
        pairs.append(
            (f"{key_prefix}DBProxyEndpointName", str(value["db_proxy_endpoint_name"]))
        )
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeDBProxyEndpointsRequest:
    out: DescribeDBProxyEndpointsRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_db_proxy_endpoint_name = el.find("DBProxyEndpointName")
    if child_db_proxy_endpoint_name is not None:
        out["db_proxy_endpoint_name"] = str(child_db_proxy_endpoint_name.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
