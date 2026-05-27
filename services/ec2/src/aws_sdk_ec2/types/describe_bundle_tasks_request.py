"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.bundle_id_string_list
    import aws_sdk_ec2.types.filter_list


class DescribeBundleTasksRequest(TypedDict):
    bundle_ids: NotRequired[
        "aws_sdk_ec2.types.bundle_id_string_list.BundleIdStringList"
    ]
    """<p>The bundle task IDs.</p> <p>Default: Describes all your bundle tasks.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>bundle-id</code> - The ID of the bundle task.</p> </li> <li> <p> <code>error-code</code> - If the task failed, the error code returned.</p> </li> <li> <p> <code>error-message</code> - If the task failed, the error message returned.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>progress</code> - The level of task completion, as a percentage (for example, 20%).</p> </li> <li> <p> <code>s3-bucket</code> - The Amazon S3 bucket to store the AMI.</p> </li> <li> <p> <code>s3-prefix</code> - The beginning of the AMI name.</p> </li> <li> <p> <code>start-time</code> - The time the task started (for example, 2013-09-15T17:15:20.000Z).</p> </li> <li> <p> <code>state</code> - The state of the task (<code>pending</code> | <code>waiting-for-shutdown</code> | <code>bundling</code> | <code>storing</code> | <code>cancelling</code> | <code>complete</code> | <code>failed</code>).</p> </li> <li> <p> <code>update-time</code> - The time of the most recent update for the task.</p> </li> </ul>"""
