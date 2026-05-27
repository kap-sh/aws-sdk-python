"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrReservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_id
    import aws_sdk_ec2.types.subnet_cidr_reservation_type
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list


class SubnetCidrReservation(TypedDict):
    subnet_cidr_reservation_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_id.SubnetCidrReservationId"
    ]
    """<p>The ID of the subnet CIDR reservation.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR that has been reserved.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_type.SubnetCidrReservationType"
    ]
    """<p>The type of reservation. </p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that owns the subnet CIDR reservation. </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description assigned to the subnet CIDR reservation.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the subnet CIDR reservation.</p>"""
