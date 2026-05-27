"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.netmask_length
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.vpc_id


class CreateSubnetRequest(TypedDict):
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the subnet.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone for the subnet.</p> <p>Default: Amazon Web Services selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.</p> <p>To create a subnet in a Local Zone, set this value to the Local Zone ID, for example <code>us-west-2-lax-1a</code>. For information about the Regions that support Local Zones, see <a href=\"https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html\">Available Local Zones</a>.</p> <p>To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The AZ ID or the Local Zone ID of the subnet.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 network range for the subnet, in CIDR notation. For example, <code>10.0.0.0/24</code>. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</p> <p>This parameter is not supported for an IPv6 only subnet.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 network range for the subnet, in CIDR notation. This parameter is required for an IPv6 only subnet.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    ipv6_native: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to create an IPv6 only subnet.</p>"""
    ipv4_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv4 IPAM pool ID for the subnet.</p>"""
    ipv4_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv4 netmask length for the subnet.</p>"""
    ipv6_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv6 IPAM pool ID for the subnet.</p>"""
    ipv6_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv6 netmask length for the subnet.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
