"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredRoutesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovered_route_set
    import capo_ec2.types.next_token


class GetIpamDiscoveredRoutesResult(TypedDict, closed=True):
    ipam_discovered_routes: NotRequired[
        "capo_ec2.types.ipam_discovered_route_set.IpamDiscoveredRouteSet"
    ]
    """<p>The discovered BGP routes.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredRoutesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_discovered_routes" in value:
        import capo_ec2.types.ipam_discovered_route_set

        capo_ec2.types.ipam_discovered_route_set.serialize_ec2_query(
            value["ipam_discovered_routes"],
            pairs,
            f"{key_prefix}IpamDiscoveredRouteSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredRoutesResult:
    out: GetIpamDiscoveredRoutesResult = {}  # type: ignore[typeddict-item]
    child_ipam_discovered_routes = el.find("ipamDiscoveredRouteSet")
    if child_ipam_discovered_routes is not None:
        import capo_ec2.types.ipam_discovered_route_set

        out["ipam_discovered_routes"] = (
            capo_ec2.types.ipam_discovered_route_set.deserialize_ec2_query(
                child_ipam_discovered_routes
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
