"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_gateway_id


class ModifyVpnConnectionRequest(TypedDict, closed=True):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the VPN connection.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway at your end of the VPN connection.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpnConnectionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "customer_gateway_id" in value:
        pairs.append((f"{prefix}.CustomerGatewayId", str(value["customer_gateway_id"])))
    if "vpn_gateway_id" in value:
        pairs.append((f"{prefix}.VpnGatewayId", str(value["vpn_gateway_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVpnConnectionRequest:
    out: ModifyVpnConnectionRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_customer_gateway_id = el.find("CustomerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_vpn_gateway_id = el.find("VpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
