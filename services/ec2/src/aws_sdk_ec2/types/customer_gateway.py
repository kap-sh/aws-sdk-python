"""Generated from Smithy shape ``com.amazonaws.ec2#CustomerGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CustomerGateway(TypedDict):
    certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the customer gateway certificate.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of customer gateway device.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the customer gateway.</p>"""
    bgp_asn_extended: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p> <p>Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code> </p>"""
    customer_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the customer gateway (<code>pending | available | deleting | deleted</code>).</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of VPN connection the customer gateway supports (<code>ipsec.1</code>).</p>"""
    ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The IP address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>PublicIpv4</code>, you can use a public IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>Ipv6</code>, you can use a public IPv6 address. </p>"""
    bgp_asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p> <p>Valid values: <code>1</code> to <code>2,147,483,647</code> </p>"""
