"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_host_reservations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class DescribeHostReservationOfferingsRequest(TypedDict):
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-family</code> - The instance family of the offering (for example, <code>m4</code>).</p> </li> <li> <p> <code>payment-option</code> - The payment option (<code>NoUpfront</code> | <code>PartialUpfront</code> | <code>AllUpfront</code>).</p> </li> </ul>"""
    max_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_host_reservations_max_results.DescribeHostReservationsMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    min_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the reservation offering.</p>"""
