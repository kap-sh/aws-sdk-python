"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class SubnetConfiguration(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    ipv4: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address to assign to the endpoint network interface in the subnet. You must provide an IPv4 address if the VPC endpoint supports IPv4.</p> <p>If you specify an IPv4 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.</p>"""
    ipv6: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address to assign to the endpoint network interface in the subnet. You must provide an IPv6 address if the VPC endpoint supports IPv6.</p> <p>If you specify an IPv6 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.</p>"""
