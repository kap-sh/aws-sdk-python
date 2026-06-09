"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnRoute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_status
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id


class ClientVpnRoute(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the route is associated.</p>"""
    destination_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the route destination.</p>"""
    target_subnet: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet through which traffic is routed.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The route type.</p>"""
    origin: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates how the route was associated with the Client VPN endpoint. <code>associate</code> indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. <code>add-route</code> indicates that the route was manually added using the <b>CreateClientVpnRoute</b> action.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_route_status.ClientVpnRouteStatus"
    ]
    """<p>The current state of the route.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the route.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment, if the route targets a Transit Gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "destination_cidr" in value:
        pairs.append((f"{prefix}.DestinationCidr", str(value["destination_cidr"])))
    if "target_subnet" in value:
        pairs.append((f"{prefix}.TargetSubnet", str(value["target_subnet"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "origin" in value:
        pairs.append((f"{prefix}.Origin", str(value["origin"])))
    if "status" in value:
        import aws_sdk_ec2.types.client_vpn_route_status

        aws_sdk_ec2.types.client_vpn_route_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ClientVpnRoute:
    out: ClientVpnRoute = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_destination_cidr = el.find("DestinationCidr")
    if child_destination_cidr is not None:
        out["destination_cidr"] = str(child_destination_cidr.text or "")
    child_target_subnet = el.find("TargetSubnet")
    if child_target_subnet is not None:
        out["target_subnet"] = str(child_target_subnet.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_origin = el.find("Origin")
    if child_origin is not None:
        out["origin"] = str(child_origin.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.client_vpn_route_status

        out["status"] = aws_sdk_ec2.types.client_vpn_route_status.deserialize_ec2_query(
            child_status
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    return out
