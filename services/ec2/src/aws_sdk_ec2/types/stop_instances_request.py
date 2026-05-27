"""Generated from Smithy shape ``com.amazonaws.ec2#StopInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_string_list


class StopInstancesRequest(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p>"""
    hibernate: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Hibernates the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successfully, a normal shutdown occurs. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html\">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p> <p> Default: <code>false</code> </p>"""
    skip_os_shutdown: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to bypass the graceful OS shutdown process when the instance is stopped.</p> <important> <p>Bypassing the graceful OS shutdown might result in data loss or corruption (for example, memory contents not flushed to disk or loss of in-flight IOs) or skipped shutdown scripts.</p> </important> <p>Default: <code>false</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Forces the instance to stop. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.</p> <p>After using this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html\">Troubleshoot Amazon EC2 instance stop issues</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""
