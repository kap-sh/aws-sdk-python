"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_accept_shared_attachments_value
    import aws_sdk_ec2.types.default_route_table_association_value
    import aws_sdk_ec2.types.default_route_table_propagation_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.encryption_support
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.multicast_support_value
    import aws_sdk_ec2.types.security_group_referencing_support_value
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpn_ecmp_support_value


class TransitGatewayOptions(TypedDict):
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.</p>"""
    transit_gateway_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The transit gateway CIDR blocks.</p>"""
    auto_accept_shared_attachments: NotRequired[
        "aws_sdk_ec2.types.auto_accept_shared_attachments_value.AutoAcceptSharedAttachmentsValue"
    ]
    """<p>Indicates whether attachment requests are automatically accepted.</p>"""
    default_route_table_association: NotRequired[
        "aws_sdk_ec2.types.default_route_table_association_value.DefaultRouteTableAssociationValue"
    ]
    """<p>Indicates whether resource attachments are automatically associated with the default association route table. Enabled by default. Either <code>defaultRouteTableAssociation</code> or <code>defaultRouteTablePropagation</code> must be set to <code>enable</code> for Amazon Web Services Transit Gateway to create the default transit gateway route table.</p>"""
    association_default_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the default association route table.</p>"""
    default_route_table_propagation: NotRequired[
        "aws_sdk_ec2.types.default_route_table_propagation_value.DefaultRouteTablePropagationValue"
    ]
    """<p>Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If <code>defaultRouteTablePropagation</code> is set to <code>enable</code>, Amazon Web Services Transit Gateway creates the default transit gateway route table.</p>"""
    propagation_default_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the default propagation route table.</p>"""
    vpn_ecmp_support: NotRequired[
        "aws_sdk_ec2.types.vpn_ecmp_support_value.VpnEcmpSupportValue"
    ]
    """<p>Indicates whether Equal Cost Multipath Protocol support is enabled.</p>"""
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Indicates whether DNS support is enabled.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p>"""
    multicast_support: NotRequired[
        "aws_sdk_ec2.types.multicast_support_value.MulticastSupportValue"
    ]
    """<p>Indicates whether multicast is enabled on the transit gateway</p>"""
    encryption_support: NotRequired[
        "aws_sdk_ec2.types.encryption_support.EncryptionSupport"
    ]
    """<p>Defines if the Transit Gateway supports VPC Encryption Control.</p>"""
