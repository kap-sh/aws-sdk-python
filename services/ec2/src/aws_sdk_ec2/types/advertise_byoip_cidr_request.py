"""Generated from Smithy shape ``com.amazonaws.ec2#AdvertiseByoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class AdvertiseByoipCidrRequest(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.</p>"""
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public 2-byte or 4-byte ASN that you want to advertise.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If you have <a href=\"https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html\">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>"""
