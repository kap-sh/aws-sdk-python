"""Generated from Smithy shape ``com.amazonaws.ec2#DetachVpnGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.vpc_id
    import capo_ec2.types.vpn_gateway_id


class DetachVpnGatewayRequest(TypedDict, closed=True):
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    vpn_gateway_id: NotRequired["capo_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DetachVpnGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpn_gateway_id" in value:
        pairs.append((f"{key_prefix}VpnGatewayId", str(value["vpn_gateway_id"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DetachVpnGatewayRequest:
    out: DetachVpnGatewayRequest = {}  # type: ignore[typeddict-item]
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpn_gateway_id = el.find("VpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
