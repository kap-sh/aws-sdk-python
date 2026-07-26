"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteClientVpnRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class DeleteClientVpnRouteRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint from which the route is to be deleted.</p>"""
    target_vpc_subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the target subnet used by the route.</p>"""
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the route to be deleted.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteClientVpnRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "target_vpc_subnet_id" in value:
        pairs.append(
            (f"{prefix}.TargetVpcSubnetId", str(value["target_vpc_subnet_id"]))
        )
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteClientVpnRouteRequest:
    out: DeleteClientVpnRouteRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_target_vpc_subnet_id = el.find("TargetVpcSubnetId")
    if child_target_vpc_subnet_id is not None:
        out["target_vpc_subnet_id"] = str(child_target_vpc_subnet_id.text or "")
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
