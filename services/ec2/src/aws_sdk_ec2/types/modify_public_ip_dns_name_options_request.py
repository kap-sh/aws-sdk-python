"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPublicIpDnsNameOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.public_ip_dns_option


class ModifyPublicIpDnsNameOptionsRequest(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>A network interface ID.</p>"""
    hostname_type: NotRequired[
        "aws_sdk_ec2.types.public_ip_dns_option.PublicIpDnsOption"
    ]
    """<p>The public hostname type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p> <ul> <li> <p> <code>public-dual-stack-dns-name</code>: A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.</p> </li> <li> <p> <code>public-ipv4-dns-name</code>: An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.</p> </li> <li> <p> <code>public-ipv6-dns-name</code>: An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. </p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
