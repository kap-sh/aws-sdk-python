"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_configuration
    import aws_sdk_ec2.types.gateway_association_state
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vgw_telemetry_list
    import aws_sdk_ec2.types.vpn_connection_options
    import aws_sdk_ec2.types.vpn_state
    import aws_sdk_ec2.types.vpn_static_route_list


class VpnConnection(TypedDict, closed=True):
    category: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The category of the VPN connection. A value of <code>VPN</code> indicates an Amazon Web Services VPN connection. A value of <code>VPN-Classic</code> indicates an Amazon Web Services Classic VPN connection.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN connection.</p>"""
    vpn_concentrator_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator associated with the VPN connection.</p>"""
    core_network_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the core network.</p>"""
    core_network_attachment_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the core network attachment.</p>"""
    gateway_association_state: NotRequired[
        "aws_sdk_ec2.types.gateway_association_state.GatewayAssociationState"
    ]
    """<p>The current state of the gateway association.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_options.VpnConnectionOptions"
    ]
    """<p>The VPN connection options.</p>"""
    routes: NotRequired["aws_sdk_ec2.types.vpn_static_route_list.VpnStaticRouteList"]
    """<p>The static routes associated with the VPN connection.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN connection.</p>"""
    vgw_telemetry: NotRequired["aws_sdk_ec2.types.vgw_telemetry_list.VgwTelemetryList"]
    """<p>Information about the VPN tunnel.</p>"""
    pre_shared_key_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret storing the pre-shared key(s) for the VPN connection.</p>"""
    vpn_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN connection.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the VPN connection.</p>"""
    customer_gateway_configuration: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_configuration.customerGatewayConfiguration"
    ]
    """<p>The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the <a>CreateVpnConnection</a> response; however, it's present in the <a>DescribeVpnConnections</a> response only if the VPN connection is in the <code>pending</code> or <code>available</code> state.</p>"""
    type: NotRequired["aws_sdk_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection.</p>"""
    customer_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer gateway at your end of the VPN connection.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "category" in value:
        pairs.append((f"{prefix}.Category", str(value["category"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "vpn_concentrator_id" in value:
        pairs.append((f"{prefix}.VpnConcentratorId", str(value["vpn_concentrator_id"])))
    if "core_network_arn" in value:
        pairs.append((f"{prefix}.CoreNetworkArn", str(value["core_network_arn"])))
    if "core_network_attachment_arn" in value:
        pairs.append(
            (
                f"{prefix}.CoreNetworkAttachmentArn",
                str(value["core_network_attachment_arn"]),
            )
        )
    if "gateway_association_state" in value:
        import aws_sdk_ec2.types.gateway_association_state

        aws_sdk_ec2.types.gateway_association_state.serialize_ec2_query(
            value["gateway_association_state"],
            pairs,
            f"{prefix}.GatewayAssociationState",
        )
    if "options" in value:
        import aws_sdk_ec2.types.vpn_connection_options

        aws_sdk_ec2.types.vpn_connection_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "routes" in value:
        import aws_sdk_ec2.types.vpn_static_route_list

        aws_sdk_ec2.types.vpn_static_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.Routes"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "vgw_telemetry" in value:
        import aws_sdk_ec2.types.vgw_telemetry_list

        aws_sdk_ec2.types.vgw_telemetry_list.serialize_ec2_query(
            value["vgw_telemetry"], pairs, f"{prefix}.VgwTelemetry"
        )
    if "pre_shared_key_arn" in value:
        pairs.append((f"{prefix}.PreSharedKeyArn", str(value["pre_shared_key_arn"])))
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.vpn_state

        aws_sdk_ec2.types.vpn_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "customer_gateway_configuration" in value:
        pairs.append(
            (
                f"{prefix}.CustomerGatewayConfiguration",
                str(value["customer_gateway_configuration"]),
            )
        )
    if "type" in value:
        import aws_sdk_ec2.types.gateway_type

        aws_sdk_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "customer_gateway_id" in value:
        pairs.append((f"{prefix}.CustomerGatewayId", str(value["customer_gateway_id"])))
    if "vpn_gateway_id" in value:
        pairs.append((f"{prefix}.VpnGatewayId", str(value["vpn_gateway_id"])))


def deserialize_ec2_query(el: Element) -> VpnConnection:
    out: VpnConnection = {}  # type: ignore[typeddict-item]
    child_category = el.find("Category")
    if child_category is not None:
        out["category"] = str(child_category.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpn_concentrator_id = el.find("VpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_core_network_arn = el.find("CoreNetworkArn")
    if child_core_network_arn is not None:
        out["core_network_arn"] = str(child_core_network_arn.text or "")
    child_core_network_attachment_arn = el.find("CoreNetworkAttachmentArn")
    if child_core_network_attachment_arn is not None:
        out["core_network_attachment_arn"] = str(
            child_core_network_attachment_arn.text or ""
        )
    child_gateway_association_state = el.find("GatewayAssociationState")
    if child_gateway_association_state is not None:
        import aws_sdk_ec2.types.gateway_association_state

        out["gateway_association_state"] = (
            aws_sdk_ec2.types.gateway_association_state.deserialize_ec2_query(
                child_gateway_association_state
            )
        )
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_ec2.types.vpn_connection_options

        out["options"] = aws_sdk_ec2.types.vpn_connection_options.deserialize_ec2_query(
            child_options
        )
    if el.find("Routes") is not None:
        import aws_sdk_ec2.types.vpn_static_route_list

        out["routes"] = aws_sdk_ec2.types.vpn_static_route_list.deserialize_ec2_query(
            el, "Routes"
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("VgwTelemetry") is not None:
        import aws_sdk_ec2.types.vgw_telemetry_list

        out["vgw_telemetry"] = (
            aws_sdk_ec2.types.vgw_telemetry_list.deserialize_ec2_query(
                el, "VgwTelemetry"
            )
        )
    child_pre_shared_key_arn = el.find("PreSharedKeyArn")
    if child_pre_shared_key_arn is not None:
        out["pre_shared_key_arn"] = str(child_pre_shared_key_arn.text or "")
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.vpn_state

        out["state"] = aws_sdk_ec2.types.vpn_state.deserialize_ec2_query(child_state)
    child_customer_gateway_configuration = el.find("CustomerGatewayConfiguration")
    if child_customer_gateway_configuration is not None:
        out["customer_gateway_configuration"] = str(
            child_customer_gateway_configuration.text or ""
        )
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.gateway_type

        out["type"] = aws_sdk_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    child_customer_gateway_id = el.find("CustomerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_vpn_gateway_id = el.find("VpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    return out
