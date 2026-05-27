"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_accept_shared_attachments_value
    import aws_sdk_ec2.types.default_route_table_association_value
    import aws_sdk_ec2.types.default_route_table_propagation_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.encryption_support_option_value
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.security_group_referencing_support_value
    import aws_sdk_ec2.types.transit_gateway_cidr_block_string_list
    import aws_sdk_ec2.types.transit_gateway_route_table_id
    import aws_sdk_ec2.types.vpn_ecmp_support_value


class ModifyTransitGatewayOptions(TypedDict):
    add_transit_gateway_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_cidr_block_string_list.TransitGatewayCidrBlockStringList"
    ]
    """<p>Adds IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR block or larger for IPv4, or a size /64 CIDR block or larger for IPv6.</p>"""
    remove_transit_gateway_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_cidr_block_string_list.TransitGatewayCidrBlockStringList"
    ]
    """<p>Removes CIDR blocks for the transit gateway.</p>"""
    vpn_ecmp_support: NotRequired[
        "aws_sdk_ec2.types.vpn_ecmp_support_value.VpnEcmpSupportValue"
    ]
    """<p>Enable or disable Equal Cost Multipath Protocol support.</p>"""
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Enable or disable DNS support.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p> <p>For more information about security group referencing, see <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security\">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    auto_accept_shared_attachments: NotRequired[
        "aws_sdk_ec2.types.auto_accept_shared_attachments_value.AutoAcceptSharedAttachmentsValue"
    ]
    """<p>Enable or disable automatic acceptance of attachment requests.</p>"""
    default_route_table_association: NotRequired[
        "aws_sdk_ec2.types.default_route_table_association_value.DefaultRouteTableAssociationValue"
    ]
    """<p>Enable or disable automatic association with the default association route table.</p>"""
    association_default_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the default association route table.</p>"""
    default_route_table_propagation: NotRequired[
        "aws_sdk_ec2.types.default_route_table_propagation_value.DefaultRouteTablePropagationValue"
    ]
    """<p>Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If <code>defaultRouteTablePropagation</code> is set to <code>enable</code>, Amazon Web Services Transit Gateway will create the default transit gateway route table.</p>"""
    propagation_default_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the default propagation route table.</p>"""
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.</p> <p>The modify ASN operation is not allowed on a transit gateway if it has the following attachments:</p> <ul> <li> <p>Dynamic VPN</p> </li> <li> <p>Static VPN</p> </li> <li> <p>Direct Connect Gateway</p> </li> <li> <p>Connect</p> </li> </ul> <p>You must first delete all transit gateway attachments configured prior to modifying the ASN on the transit gateway.</p>"""
    encryption_support: NotRequired[
        "aws_sdk_ec2.types.encryption_support_option_value.EncryptionSupportOptionValue"
    ]
    """<p>Enable or disable encryption support for VPC Encryption Control.</p>"""
