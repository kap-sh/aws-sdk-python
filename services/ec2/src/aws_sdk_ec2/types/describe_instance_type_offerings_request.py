"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypeOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dito_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.location_type
    import aws_sdk_ec2.types.next_token


class DescribeInstanceTypeOfferingsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    location_type: NotRequired["aws_sdk_ec2.types.location_type.LocationType"]
    """<p>The location type.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone. When you specify a location filter, it must be an Availability Zone for the current Region.</p> </li> <li> <p> <code>availability-zone-id</code> - The AZ ID. When you specify a location filter, it must be an AZ ID for the current Region.</p> </li> <li> <p> <code>outpost</code> - The Outpost ARN. When you specify a location filter, it must be an Outpost ARN for the current Region.</p> </li> <li> <p> <code>region</code> - The current Region. If you specify a location filter, it must match the current Region.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>instance-type</code> - The instance type. For a list of possible values, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Instance.html\">Instance</a>.</p> </li> <li> <p> <code>location</code> - The location. For a list of possible identifiers, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html\">Regions and Zones</a>.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.dito_max_results.DITOMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
