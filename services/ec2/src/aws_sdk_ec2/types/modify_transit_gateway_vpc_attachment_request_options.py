"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayVpcAttachmentRequestOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.appliance_mode_support_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.ipv6_support_value
    import aws_sdk_ec2.types.security_group_referencing_support_value


class ModifyTransitGatewayVpcAttachmentRequestOptions(TypedDict):
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Enable or disable DNS support. The default is <code>enable</code>.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management. </p> <p>This option is disabled by default.</p> <p>For more information about security group referencing, see <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security\">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    ipv6_support: NotRequired["aws_sdk_ec2.types.ipv6_support_value.Ipv6SupportValue"]
    """<p>Enable or disable IPv6 support. The default is <code>enable</code>.</p>"""
    appliance_mode_support: NotRequired[
        "aws_sdk_ec2.types.appliance_mode_support_value.ApplianceModeSupportValue"
    ]
    """<p>Enable or disable support for appliance mode. If enabled, a traffic flow between a source and destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow. The default is <code>disable</code>.</p>"""
