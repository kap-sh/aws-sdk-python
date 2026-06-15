"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRequestOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_accept_shared_attachments_value
    import aws_sdk_ec2.types.default_route_table_association_value
    import aws_sdk_ec2.types.default_route_table_propagation_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.multicast_support_value
    import aws_sdk_ec2.types.security_group_referencing_support_value
    import aws_sdk_ec2.types.transit_gateway_cidr_block_string_list
    import aws_sdk_ec2.types.vpn_ecmp_support_value


class TransitGatewayRequestOptions(TypedDict):
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs. The default is <code>64512</code>.</p>"""
    auto_accept_shared_attachments: NotRequired[
        "aws_sdk_ec2.types.auto_accept_shared_attachments_value.AutoAcceptSharedAttachmentsValue"
    ]
    """<p>Enable or disable automatic acceptance of attachment requests. Disabled by default.</p>"""
    default_route_table_association: NotRequired[
        "aws_sdk_ec2.types.default_route_table_association_value.DefaultRouteTableAssociationValue"
    ]
    """<p>Enable or disable automatic association with the default association route table. Enabled by default.</p>"""
    default_route_table_propagation: NotRequired[
        "aws_sdk_ec2.types.default_route_table_propagation_value.DefaultRouteTablePropagationValue"
    ]
    """<p>Enable or disable automatic propagation of routes to the default propagation route table. Enabled by default.</p>"""
    vpn_ecmp_support: NotRequired[
        "aws_sdk_ec2.types.vpn_ecmp_support_value.VpnEcmpSupportValue"
    ]
    """<p>Enable or disable Equal Cost Multipath Protocol support. Enabled by default.</p>"""
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Enable or disable DNS support. Enabled by default.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    r"""<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p> <p>For more information about security group referencing, see <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security\">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    multicast_support: NotRequired[
        "aws_sdk_ec2.types.multicast_support_value.MulticastSupportValue"
    ]
    """<p>Indicates whether multicast is enabled on the transit gateway</p>"""
    transit_gateway_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_cidr_block_string_list.TransitGatewayCidrBlockStringList"
    ]
    """<p>One or more IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR block or larger for IPv4, or a size /64 CIDR block or larger for IPv6.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRequestOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "amazon_side_asn" in value:
        pairs.append((f"{prefix}.AmazonSideAsn", str(value["amazon_side_asn"])))
    if "auto_accept_shared_attachments" in value:
        import aws_sdk_ec2.types.auto_accept_shared_attachments_value

        aws_sdk_ec2.types.auto_accept_shared_attachments_value.serialize_ec2_query(
            value["auto_accept_shared_attachments"],
            pairs,
            f"{prefix}.AutoAcceptSharedAttachments",
        )
    if "default_route_table_association" in value:
        import aws_sdk_ec2.types.default_route_table_association_value

        aws_sdk_ec2.types.default_route_table_association_value.serialize_ec2_query(
            value["default_route_table_association"],
            pairs,
            f"{prefix}.DefaultRouteTableAssociation",
        )
    if "default_route_table_propagation" in value:
        import aws_sdk_ec2.types.default_route_table_propagation_value

        aws_sdk_ec2.types.default_route_table_propagation_value.serialize_ec2_query(
            value["default_route_table_propagation"],
            pairs,
            f"{prefix}.DefaultRouteTablePropagation",
        )
    if "vpn_ecmp_support" in value:
        import aws_sdk_ec2.types.vpn_ecmp_support_value

        aws_sdk_ec2.types.vpn_ecmp_support_value.serialize_ec2_query(
            value["vpn_ecmp_support"], pairs, f"{prefix}.VpnEcmpSupport"
        )
    if "dns_support" in value:
        import aws_sdk_ec2.types.dns_support_value

        aws_sdk_ec2.types.dns_support_value.serialize_ec2_query(
            value["dns_support"], pairs, f"{prefix}.DnsSupport"
        )
    if "security_group_referencing_support" in value:
        import aws_sdk_ec2.types.security_group_referencing_support_value

        aws_sdk_ec2.types.security_group_referencing_support_value.serialize_ec2_query(
            value["security_group_referencing_support"],
            pairs,
            f"{prefix}.SecurityGroupReferencingSupport",
        )
    if "multicast_support" in value:
        import aws_sdk_ec2.types.multicast_support_value

        aws_sdk_ec2.types.multicast_support_value.serialize_ec2_query(
            value["multicast_support"], pairs, f"{prefix}.MulticastSupport"
        )
    if "transit_gateway_cidr_blocks" in value:
        import aws_sdk_ec2.types.transit_gateway_cidr_block_string_list

        aws_sdk_ec2.types.transit_gateway_cidr_block_string_list.serialize_ec2_query(
            value["transit_gateway_cidr_blocks"],
            pairs,
            f"{prefix}.TransitGatewayCidrBlocks",
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRequestOptions:
    out: TransitGatewayRequestOptions = {}  # type: ignore[typeddict-item]
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_auto_accept_shared_attachments = el.find("AutoAcceptSharedAttachments")
    if child_auto_accept_shared_attachments is not None:
        import aws_sdk_ec2.types.auto_accept_shared_attachments_value

        out["auto_accept_shared_attachments"] = (
            aws_sdk_ec2.types.auto_accept_shared_attachments_value.deserialize_ec2_query(
                child_auto_accept_shared_attachments
            )
        )
    child_default_route_table_association = el.find("DefaultRouteTableAssociation")
    if child_default_route_table_association is not None:
        import aws_sdk_ec2.types.default_route_table_association_value

        out["default_route_table_association"] = (
            aws_sdk_ec2.types.default_route_table_association_value.deserialize_ec2_query(
                child_default_route_table_association
            )
        )
    child_default_route_table_propagation = el.find("DefaultRouteTablePropagation")
    if child_default_route_table_propagation is not None:
        import aws_sdk_ec2.types.default_route_table_propagation_value

        out["default_route_table_propagation"] = (
            aws_sdk_ec2.types.default_route_table_propagation_value.deserialize_ec2_query(
                child_default_route_table_propagation
            )
        )
    child_vpn_ecmp_support = el.find("VpnEcmpSupport")
    if child_vpn_ecmp_support is not None:
        import aws_sdk_ec2.types.vpn_ecmp_support_value

        out["vpn_ecmp_support"] = (
            aws_sdk_ec2.types.vpn_ecmp_support_value.deserialize_ec2_query(
                child_vpn_ecmp_support
            )
        )
    child_dns_support = el.find("DnsSupport")
    if child_dns_support is not None:
        import aws_sdk_ec2.types.dns_support_value

        out["dns_support"] = aws_sdk_ec2.types.dns_support_value.deserialize_ec2_query(
            child_dns_support
        )
    child_security_group_referencing_support = el.find(
        "SecurityGroupReferencingSupport"
    )
    if child_security_group_referencing_support is not None:
        import aws_sdk_ec2.types.security_group_referencing_support_value

        out["security_group_referencing_support"] = (
            aws_sdk_ec2.types.security_group_referencing_support_value.deserialize_ec2_query(
                child_security_group_referencing_support
            )
        )
    child_multicast_support = el.find("MulticastSupport")
    if child_multicast_support is not None:
        import aws_sdk_ec2.types.multicast_support_value

        out["multicast_support"] = (
            aws_sdk_ec2.types.multicast_support_value.deserialize_ec2_query(
                child_multicast_support
            )
        )
    if el.find("TransitGatewayCidrBlocks") is not None:
        import aws_sdk_ec2.types.transit_gateway_cidr_block_string_list

        out["transit_gateway_cidr_blocks"] = (
            aws_sdk_ec2.types.transit_gateway_cidr_block_string_list.deserialize_ec2_query(
                el, "TransitGatewayCidrBlocks"
            )
        )
    return out
