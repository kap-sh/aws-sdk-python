"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionByoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.cidr_authorization_context
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class ProvisionByoipCidrRequest(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public IPv4 or IPv6 address range, in CIDR notation. The most specific IPv4 prefix that you can specify is /24. The most specific IPv6 address range that you can bring is /48 for CIDRs that are publicly advertisable and /56 for CIDRs that are not publicly advertisable. The address range cannot overlap with another address range that you've brought to this or another Region.</p>"""
    cidr_authorization_context: NotRequired[
        "aws_sdk_ec2.types.cidr_authorization_context.CidrAuthorizationContext"
    ]
    """<p>A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.</p>"""
    publicly_advertisable: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(IPv6 only) Indicate whether the address range will be publicly advertised to the internet.</p> <p>Default: true</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the address range and the address pool.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    pool_tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the address pool.</p>"""
    multi_region: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Reserved.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If you have <a href=\"https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html\">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>"""
