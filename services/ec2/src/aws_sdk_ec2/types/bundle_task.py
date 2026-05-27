"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task_error
    import aws_sdk_ec2.types.bundle_task_state
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.storage
    import aws_sdk_ec2.types.string


class BundleTask(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance associated with this bundle task.</p>"""
    bundle_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the bundle task.</p>"""
    state: NotRequired["aws_sdk_ec2.types.bundle_task_state.BundleTaskState"]
    """<p>The state of the task.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time this task started.</p>"""
    update_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time of the most recent update for the task.</p>"""
    storage: NotRequired["aws_sdk_ec2.types.storage.Storage"]
    """<p>The Amazon S3 storage locations.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The level of task completion, as a percent (for example, 20%).</p>"""
    bundle_task_error: NotRequired[
        "aws_sdk_ec2.types.bundle_task_error.BundleTaskError"
    ]
    """<p>If the task fails, a description of the error.</p>"""
