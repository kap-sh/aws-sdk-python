"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.describe_capacity_block_extension_offerings_max_results
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockExtensionOfferingsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The duration of the Capacity Block extension offering in hours.</p>"""
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity reservation to be extended.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_block_extension_offerings_max_results.DescribeCapacityBlockExtensionOfferingsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
