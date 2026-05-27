"""Generated from Smithy shape ``com.amazonaws.ec2#GetSubnetCidrReservationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_list


class GetSubnetCidrReservationsResult(TypedDict):
    subnet_ipv4_cidr_reservations: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_list.SubnetCidrReservationList"
    ]
    """<p>Information about the IPv4 subnet CIDR reservations.</p>"""
    subnet_ipv6_cidr_reservations: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_list.SubnetCidrReservationList"
    ]
    """<p>Information about the IPv6 subnet CIDR reservations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
