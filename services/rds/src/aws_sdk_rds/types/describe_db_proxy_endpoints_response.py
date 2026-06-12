"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxyEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_endpoint_list
    import aws_sdk_rds.types.string


class DescribeDBProxyEndpointsResponse(TypedDict):
    db_proxy_endpoints: NotRequired[
        "aws_sdk_rds.types.db_proxy_endpoint_list.DBProxyEndpointList"
    ]
    """<p>The list of <code>ProxyEndpoint</code> objects returned by the API operation.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxyEndpointsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_endpoints" in value:
        import aws_sdk_rds.types.db_proxy_endpoint_list

        aws_sdk_rds.types.db_proxy_endpoint_list.serialize_query(
            value["db_proxy_endpoints"], pairs, f"{prefix}.DBProxyEndpoints"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBProxyEndpointsResponse:
    out: DescribeDBProxyEndpointsResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoints = el.find("DBProxyEndpoints")
    if child_db_proxy_endpoints is not None:
        import aws_sdk_rds.types.db_proxy_endpoint_list

        out["db_proxy_endpoints"] = (
            aws_sdk_rds.types.db_proxy_endpoint_list.deserialize_query(
                child_db_proxy_endpoints
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
