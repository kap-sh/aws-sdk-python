"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeClientVpnIngressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.string


class RevokeClientVpnIngressRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint with which the authorization rule is associated.</p>"""
    target_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network for which access is being removed.</p>"""
    access_group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Active Directory group for which to revoke access. </p>"""
    revoke_all_groups: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether access should be revoked for all groups for a single <code>TargetNetworkCidr</code> that earlier authorized ingress for all groups using <code>AuthorizeAllGroups</code>. This does not impact other authorization rules that allowed ingress to the same <code>TargetNetworkCidr</code> with a specific <code>AccessGroupId</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RevokeClientVpnIngressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "target_network_cidr" in value:
        pairs.append((f"{prefix}.TargetNetworkCidr", str(value["target_network_cidr"])))
    if "access_group_id" in value:
        pairs.append((f"{prefix}.AccessGroupId", str(value["access_group_id"])))
    if "revoke_all_groups" in value:
        pairs.append(
            (
                f"{prefix}.RevokeAllGroups",
                "true" if value["revoke_all_groups"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> RevokeClientVpnIngressRequest:
    out: RevokeClientVpnIngressRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_target_network_cidr = el.find("TargetNetworkCidr")
    if child_target_network_cidr is not None:
        out["target_network_cidr"] = str(child_target_network_cidr.text or "")
    child_access_group_id = el.find("AccessGroupId")
    if child_access_group_id is not None:
        out["access_group_id"] = str(child_access_group_id.text or "")
    child_revoke_all_groups = el.find("RevokeAllGroups")
    if child_revoke_all_groups is not None:
        out["revoke_all_groups"] = (
            child_revoke_all_groups.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
