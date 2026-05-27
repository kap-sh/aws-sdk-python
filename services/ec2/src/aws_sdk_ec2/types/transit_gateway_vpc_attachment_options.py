"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachmentOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.appliance_mode_support_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.ipv6_support_value
    import aws_sdk_ec2.types.security_group_referencing_support_value


class TransitGatewayVpcAttachmentOptions(TypedDict):
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Indicates whether DNS support is enabled.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.</p> <p>This option is enabled by default.</p> <p>For more information about security group referencing, see <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security\">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    ipv6_support: NotRequired["aws_sdk_ec2.types.ipv6_support_value.Ipv6SupportValue"]
    """<p>Indicates whether IPv6 support is disabled.</p>"""
    appliance_mode_support: NotRequired[
        "aws_sdk_ec2.types.appliance_mode_support_value.ApplianceModeSupportValue"
    ]
    """<p>Indicates whether appliance mode support is enabled.</p>"""
