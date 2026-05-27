"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_reservation_set
    import aws_sdk_ec2.types.string


class DescribeHostReservationsResult(TypedDict):
    host_reservation_set: NotRequired[
        "aws_sdk_ec2.types.host_reservation_set.HostReservationSet"
    ]
    """<p>Details about the reservation's configuration.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
