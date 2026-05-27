"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeTagsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>key</code> - The tag key.</p> </li> <li> <p> <code>resource-id</code> - The ID of the resource.</p> </li> <li> <p> <code>resource-type</code> - The resource type. For a list of possible values, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TagSpecification.html\">TagSpecification</a>.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of the tag. For example, specify \"tag:Owner\" for the filter name and \"TeamA\" for the filter value to find resources with the tag \"Owner=TeamA\".</p> </li> <li> <p> <code>value</code> - The tag value.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. This value can be between 5 and 1000. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
