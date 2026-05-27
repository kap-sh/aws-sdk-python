"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReplaceRootVolumeTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.replace_root_volume_task_ids


class DescribeReplaceRootVolumeTasksRequest(TypedDict):
    replace_root_volume_task_ids: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_task_ids.ReplaceRootVolumeTaskIds"
    ]
    """<p>The ID of the root volume replacement task to view.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Filter to use:</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance for which the root volume replacement task was created.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_replace_root_volume_tasks_max_results.DescribeReplaceRootVolumeTasksMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
