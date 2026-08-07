"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAccessList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.endpoint_accesses
    import capo_redshift.types.string


class EndpointAccessList(TypedDict, closed=True):
    endpoint_access_list: NotRequired[
        "capo_redshift.types.endpoint_accesses.EndpointAccesses"
    ]
    """<p>The list of endpoints with access to the cluster.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeEndpointAccess</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAccessList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "endpoint_access_list" in value:
        import capo_redshift.types.endpoint_accesses

        capo_redshift.types.endpoint_accesses.serialize_query(
            value["endpoint_access_list"], pairs, f"{key_prefix}EndpointAccessList"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> EndpointAccessList:
    out: EndpointAccessList = {}  # type: ignore[typeddict-item]
    child_endpoint_access_list = el.find("EndpointAccessList")
    if child_endpoint_access_list is not None:
        import capo_redshift.types.endpoint_accesses

        out["endpoint_access_list"] = (
            capo_redshift.types.endpoint_accesses.deserialize_query(
                child_endpoint_access_list
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
