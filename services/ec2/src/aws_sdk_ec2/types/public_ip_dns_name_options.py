"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpDnsNameOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PublicIpDnsNameOptions(TypedDict):
    dns_hostname_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public hostname type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_ipv4_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.</p>"""
    public_ipv6_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.</p>"""
    public_dual_stack_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.</p>"""
