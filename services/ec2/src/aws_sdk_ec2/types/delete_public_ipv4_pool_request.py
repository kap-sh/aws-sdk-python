"""Generated from Smithy shape ``com.amazonaws.ec2#DeletePublicIpv4PoolRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipv4_pool_ec2_id
    import aws_sdk_ec2.types.string


class DeletePublicIpv4PoolRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the public IPv4 pool you want to delete.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail\">Local Zone availability</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
