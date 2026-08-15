"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamRouteProtectionFindingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_route_protection_finding_set
    import capo_ec2.types.next_token


class GetIpamRouteProtectionFindingsResult(TypedDict, closed=True):
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM.</p>"""
    route_protection_findings: NotRequired[
        "capo_ec2.types.ipam_route_protection_finding_set.IpamRouteProtectionFindingSet"
    ]
    """<p>The route protection findings.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamRouteProtectionFindingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "route_protection_findings" in value:
        import capo_ec2.types.ipam_route_protection_finding_set

        capo_ec2.types.ipam_route_protection_finding_set.serialize_ec2_query(
            value["route_protection_findings"],
            pairs,
            f"{key_prefix}RouteProtectionFindingSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamRouteProtectionFindingsResult:
    out: GetIpamRouteProtectionFindingsResult = {}  # type: ignore[typeddict-item]
    child_ipam_id = el.find("ipamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_route_protection_findings = el.find("routeProtectionFindingSet")
    if child_route_protection_findings is not None:
        import capo_ec2.types.ipam_route_protection_finding_set

        out["route_protection_findings"] = (
            capo_ec2.types.ipam_route_protection_finding_set.deserialize_ec2_query(
                child_route_protection_findings
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
