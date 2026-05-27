"""Generated from Smithy shape ``com.amazonaws.ec2#ConversionTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task_state
    import aws_sdk_ec2.types.import_instance_task_details
    import aws_sdk_ec2.types.import_volume_task_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ConversionTask(TypedDict):
    conversion_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the conversion task.</p>"""
    expiration_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The time when the task expires. If the upload isn't complete before the expiration time, we automatically cancel the task.</p>"""
    import_instance: NotRequired[
        "aws_sdk_ec2.types.import_instance_task_details.ImportInstanceTaskDetails"
    ]
    """<p>If the task is for importing an instance, this contains information about the import instance task.</p>"""
    import_volume: NotRequired[
        "aws_sdk_ec2.types.import_volume_task_details.ImportVolumeTaskDetails"
    ]
    """<p>If the task is for importing a volume, this contains information about the import volume task.</p>"""
    state: NotRequired["aws_sdk_ec2.types.conversion_task_state.ConversionTaskState"]
    """<p>The state of the conversion task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message related to the conversion task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the task.</p>"""
