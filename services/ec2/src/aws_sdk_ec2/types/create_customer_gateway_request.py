"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCustomerGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateCustomerGatewayRequest(TypedDict):
    bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Default: 65000</p> <p>Valid values: <code>1</code> to <code>2,147,483,647</code> </p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> <i>This member has been deprecated.</i> The Internet-routable IP address for the customer gateway's outside interface. The address must be static.</p>"""
    certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the customer gateway certificate.</p>"""
    type: NotRequired["aws_sdk_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the customer gateway.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the customer gateway device.</p> <p>Length Constraints: Up to 255 characters.</p>"""
    ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>Ipv6</code>, you can use an IPv6 address. </p>"""
    bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
