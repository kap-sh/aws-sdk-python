"""Generated from Smithy shape ``com.amazonaws.ec2#StoreImageTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class StoreImageTaskResult(TypedDict):
    ami_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI that is being stored.</p>"""
    task_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time the task started.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket that contains the stored AMI object.</p>"""
    s3object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the bucket.</p>"""
    progress_percentage: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The progress of the task as a percentage.</p>"""
    store_task_state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the store task (<code>InProgress</code>, <code>Completed</code>, or <code>Failed</code>).</p>"""
    store_task_failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the tasks fails, the reason for the failure is returned. If the task succeeds, <code>null</code> is returned.</p>"""
