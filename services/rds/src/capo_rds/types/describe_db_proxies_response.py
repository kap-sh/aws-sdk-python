"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_list
    import capo_rds.types.string


class DescribeDBProxiesResponse(TypedDict, closed=True):
    db_proxies: NotRequired["capo_rds.types.db_proxy_list.DBProxyList"]
    """<p>A return value representing an arbitrary number of <code>DBProxy</code> data structures.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxiesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxies" in value:
        import capo_rds.types.db_proxy_list

        capo_rds.types.db_proxy_list.serialize_query(
            value["db_proxies"], pairs, f"{prefix}.DBProxies"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBProxiesResponse:
    out: DescribeDBProxiesResponse = {}  # type: ignore[typeddict-item]
    child_db_proxies = el.find("DBProxies")
    if child_db_proxies is not None:
        import capo_rds.types.db_proxy_list

        out["db_proxies"] = capo_rds.types.db_proxy_list.deserialize_query(
            child_db_proxies
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
