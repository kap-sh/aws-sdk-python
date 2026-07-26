"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAuthorizationList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.endpoint_authorizations
    import capo_redshift.types.string


class EndpointAuthorizationList(TypedDict, closed=True):
    endpoint_authorization_list: NotRequired[
        "capo_redshift.types.endpoint_authorizations.EndpointAuthorizations"
    ]
    """<p>The authorizations to an endpoint.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeEndpointAuthorization</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAuthorizationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "endpoint_authorization_list" in value:
        import capo_redshift.types.endpoint_authorizations

        capo_redshift.types.endpoint_authorizations.serialize_query(
            value["endpoint_authorization_list"],
            pairs,
            f"{prefix}.EndpointAuthorizationList",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> EndpointAuthorizationList:
    out: EndpointAuthorizationList = {}  # type: ignore[typeddict-item]
    child_endpoint_authorization_list = el.find("EndpointAuthorizationList")
    if child_endpoint_authorization_list is not None:
        import capo_redshift.types.endpoint_authorizations

        out["endpoint_authorization_list"] = (
            capo_redshift.types.endpoint_authorizations.deserialize_query(
                child_endpoint_authorization_list
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
