"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetCidrReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_type
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class CreateSubnetCidrReservationRequest(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 or IPV6 CIDR range to reserve.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_type.SubnetCidrReservationType"
    ]
    """<p>The type of reservation. The reservation type determines how the reserved IP addresses are assigned to resources.</p> <ul> <li> <p> <code>prefix</code> - Amazon Web Services assigns the reserved IP addresses to network interfaces.</p> </li> <li> <p> <code>explicit</code> - You assign the reserved IP addresses to network interfaces.</p> </li> </ul>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description to assign to the subnet CIDR reservation.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the subnet CIDR reservation.</p>"""
