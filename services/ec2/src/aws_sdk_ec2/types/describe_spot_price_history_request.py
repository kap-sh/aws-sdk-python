"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotPriceHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_type_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.product_description_list
    import aws_sdk_ec2.types.string


class DescribeSpotPriceHistoryRequest(TypedDict):
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>Filters the results by the specified ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    instance_types: NotRequired["aws_sdk_ec2.types.instance_type_list.InstanceTypeList"]
    """<p>Filters the results by the specified instance types.</p>"""
    product_descriptions: NotRequired[
        "aws_sdk_ec2.types.product_description_list.ProductDescriptionList"
    ]
    """<p>Filters the results by the specified basic product descriptions.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone for which prices should be returned.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone for which prices should be returned.</p> </li> <li> <p> <code>instance-type</code> - The type of instance (for example, <code>m3.medium</code>).</p> </li> <li> <p> <code>product-description</code> - The product description for the Spot price (<code>Linux/UNIX</code> | <code>Red Hat Enterprise Linux</code> | <code>SUSE Linux</code> | <code>Windows</code> | <code>Linux/UNIX (Amazon VPC)</code> | <code>Red Hat Enterprise Linux (Amazon VPC)</code> | <code>SUSE Linux (Amazon VPC)</code> | <code>Windows (Amazon VPC)</code>).</p> </li> <li> <p> <code>spot-price</code> - The Spot price. The value must match exactly (or use wildcards; greater than or less than comparison is not supported).</p> </li> <li> <p> <code>timestamp</code> - The time stamp of the Spot price history, in UTC format (for example, <i>ddd MMM dd HH</i>:<i>mm</i>:<i>ss</i> UTC <i>YYYY</i>). You can use wildcards (<code>*</code> and <code>?</code>). Greater than or less than comparison is not supported.</p> </li> </ul>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Filters the results by the specified Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
