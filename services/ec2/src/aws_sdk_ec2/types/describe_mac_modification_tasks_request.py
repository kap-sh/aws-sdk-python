"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacModificationTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_mac_modification_tasks_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.mac_modification_task_id_list
    import aws_sdk_ec2.types.string


class DescribeMacModificationTasksRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Specifies one or more filters for the request:</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance for which the task was created.</p> </li> <li> <p> <code>task-state</code> - The state of the task (<code>successful</code> | <code>failed</code> | <code>in-progress</code> | <code>pending</code>).</p> </li> <li> <p> <code>mac-system-integrity-protection-configuration.sip-status</code> - The overall SIP state requested in the task (<code>enabled</code> | <code>disabled</code>).</p> </li> <li> <p> <code>start-time</code> - The date and time the task was created.</p> </li> <li> <p> <code>task-type</code> - The type of task (<code>sip-modification</code> | <code>volume-ownership-delegation</code>).</p> </li> </ul>"""
    mac_modification_task_ids: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task_id_list.MacModificationTaskIdList"
    ]
    """<p>The ID of task.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_mac_modification_tasks_max_results.DescribeMacModificationTasksMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
