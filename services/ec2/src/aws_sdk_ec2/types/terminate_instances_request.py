"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_string_list


class TerminateInstancesRequest(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p> <p>Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Forces the instances to terminate. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.</p>"""
    skip_os_shutdown: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to bypass the graceful OS shutdown process when the instance is terminated.</p> <p>Default: <code>false</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
