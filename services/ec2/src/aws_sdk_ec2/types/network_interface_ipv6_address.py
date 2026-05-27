"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIpv6Address``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class NetworkInterfaceIpv6Address(TypedDict):
    ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address.</p>"""
    public_ipv6_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    is_primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html\">ModifyNetworkInterfaceAttribute</a>.</p>"""
