"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStoreImageTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_store_image_tasks_request_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.image_id_list
    import aws_sdk_ec2.types.string


class DescribeStoreImageTasksRequest(TypedDict):
    image_ids: NotRequired["aws_sdk_ec2.types.image_id_list.ImageIdList"]
    """<p>The AMI IDs for which to show progress. Up to 20 AMI IDs can be included in a request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>task-state</code> - Returns tasks in a certain state (<code>InProgress</code> | <code>Completed</code> | <code>Failed</code>)</p> </li> <li> <p> <code>bucket</code> - Returns task information for tasks that targeted a specific bucket. For the filter value, specify the bucket name.</p> </li> </ul> <note> <p>When you specify the <code>ImageIds</code> parameter, any filters that you specify are ignored. To use the filters, you must remove the <code>ImageIds</code> parameter.</p> </note>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_store_image_tasks_request_max_results.DescribeStoreImageTasksRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p> <p>You cannot specify this parameter and the <code>ImageIds</code> parameter in the same call.</p>"""
