"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamRouteOriginAuthorizationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_route_origin_authorization_info_set
    import capo_ec2.types.next_token


class GetIpamRouteOriginAuthorizationsResult(TypedDict, closed=True):
    ipam_route_origin_authorizations: NotRequired[
        "capo_ec2.types.ipam_route_origin_authorization_info_set.IpamRouteOriginAuthorizationInfoSet"
    ]
    """<p>The Route Origin Authorizations published to the RPKI.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamRouteOriginAuthorizationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_route_origin_authorizations" in value:
        import capo_ec2.types.ipam_route_origin_authorization_info_set

        capo_ec2.types.ipam_route_origin_authorization_info_set.serialize_ec2_query(
            value["ipam_route_origin_authorizations"],
            pairs,
            f"{key_prefix}IpamRouteOriginAuthorizationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamRouteOriginAuthorizationsResult:
    out: GetIpamRouteOriginAuthorizationsResult = {}  # type: ignore[typeddict-item]
    child_ipam_route_origin_authorizations = el.find("ipamRouteOriginAuthorizationSet")
    if child_ipam_route_origin_authorizations is not None:
        import capo_ec2.types.ipam_route_origin_authorization_info_set

        out["ipam_route_origin_authorizations"] = (
            capo_ec2.types.ipam_route_origin_authorization_info_set.deserialize_ec2_query(
                child_ipam_route_origin_authorizations
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
