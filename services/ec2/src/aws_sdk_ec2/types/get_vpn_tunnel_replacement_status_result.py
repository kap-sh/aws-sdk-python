"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnTunnelReplacementStatusResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.maintenance_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_gateway_id


class GetVpnTunnelReplacementStatusResult(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Site-to-Site VPN connection. </p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway associated with the VPN connection.</p>"""
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    maintenance_details: NotRequired[
        "aws_sdk_ec2.types.maintenance_details.MaintenanceDetails"
    ]
    """<p>Get details of pending tunnel endpoint maintenance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnTunnelReplacementStatusResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "customer_gateway_id" in value:
        pairs.append((f"{prefix}.CustomerGatewayId", str(value["customer_gateway_id"])))
    if "vpn_gateway_id" in value:
        pairs.append((f"{prefix}.VpnGatewayId", str(value["vpn_gateway_id"])))
    if "vpn_tunnel_outside_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.VpnTunnelOutsideIpAddress",
                str(value["vpn_tunnel_outside_ip_address"]),
            )
        )
    if "maintenance_details" in value:
        import aws_sdk_ec2.types.maintenance_details

        aws_sdk_ec2.types.maintenance_details.serialize_ec2_query(
            value["maintenance_details"], pairs, f"{prefix}.MaintenanceDetails"
        )


def deserialize_ec2_query(el: Element) -> GetVpnTunnelReplacementStatusResult:
    out: GetVpnTunnelReplacementStatusResult = {}  # type: ignore[typeddict-item]
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
    child_vpn_tunnel_outside_ip_address = el.find("VpnTunnelOutsideIpAddress")
    if child_vpn_tunnel_outside_ip_address is not None:
        out["vpn_tunnel_outside_ip_address"] = str(
            child_vpn_tunnel_outside_ip_address.text or ""
        )
    child_maintenance_details = el.find("MaintenanceDetails")
    if child_maintenance_details is not None:
        import aws_sdk_ec2.types.maintenance_details

        out["maintenance_details"] = (
            aws_sdk_ec2.types.maintenance_details.deserialize_ec2_query(
                child_maintenance_details
            )
        )
    return out
