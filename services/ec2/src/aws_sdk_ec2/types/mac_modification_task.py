"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.mac_modification_task_id
    import aws_sdk_ec2.types.mac_modification_task_state
    import aws_sdk_ec2.types.mac_modification_task_type
    import aws_sdk_ec2.types.mac_system_integrity_protection_configuration
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.tag_list


class MacModificationTask(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the Amazon EC2 Mac instance.</p>"""
    mac_modification_task_id: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task_id.MacModificationTaskId"
    ]
    """<p>The ID of task.</p>"""
    mac_system_integrity_protection_config: NotRequired[
        "aws_sdk_ec2.types.mac_system_integrity_protection_configuration.MacSystemIntegrityProtectionConfiguration"
    ]
    """<p>[SIP modification tasks only] Information about the SIP configuration.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the task was created, in the UTC timezone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the task.</p>"""
    task_state: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task_state.MacModificationTaskState"
    ]
    """<p>The state of the task.</p>"""
    task_type: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task_type.MacModificationTaskType"
    ]
    """<p>The type of task.</p>"""
