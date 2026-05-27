"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.replace_root_volume_task_id
    import aws_sdk_ec2.types.replace_root_volume_task_state
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ReplaceRootVolumeTask(TypedDict):
    replace_root_volume_task_id: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_task_id.ReplaceRootVolumeTaskId"
    ]
    """<p>The ID of the root volume replacement task.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance for which the root volume replacement task was created.</p>"""
    task_state: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_task_state.ReplaceRootVolumeTaskState"
    ]
    """<p>The state of the task. The task can be in one of the following states:</p> <ul> <li> <p> <code>pending</code> - the replacement volume is being created.</p> </li> <li> <p> <code>in-progress</code> - the original volume is being detached and the replacement volume is being attached.</p> </li> <li> <p> <code>succeeded</code> - the replacement volume has been successfully attached to the instance and the instance is available.</p> </li> <li> <p> <code>failing</code> - the replacement task is in the process of failing.</p> </li> <li> <p> <code>failed</code> - the replacement task has failed but the original root volume is still attached.</p> </li> <li> <p> <code>failing-detached</code> - the replacement task is in the process of failing. The instance might have no root volume attached.</p> </li> <li> <p> <code>failed-detached</code> - the replacement task has failed and the instance has no root volume attached.</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The time the task was started.</p>"""
    complete_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The time the task completed.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the task.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI used to create the replacement root volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot used to create the replacement root volume.</p>"""
    delete_replaced_root_volume: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the original root volume is to be deleted after the root volume replacement task completes.</p>"""
