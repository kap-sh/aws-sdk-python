"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastLaunchResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fast_launch_launch_template_specification_response
    import aws_sdk_ec2.types.fast_launch_resource_type
    import aws_sdk_ec2.types.fast_launch_snapshot_configuration_response
    import aws_sdk_ec2.types.fast_launch_state_code
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class DisableFastLaunchResult(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image for which Windows fast launch was disabled.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.fast_launch_resource_type.FastLaunchResourceType"
    ]
    """<p>The pre-provisioning resource type that must be cleaned after turning off Windows fast launch for the Windows AMI. Supported values include: <code>snapshot</code>.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.FastLaunchSnapshotConfigurationResponse"
    ]
    """<p>Parameters that were used for Windows fast launch for the Windows AMI before Windows fast launch was disabled. This informs the clean-up process.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_response.FastLaunchLaunchTemplateSpecificationResponse"
    ]
    """<p>The launch template that was used to launch Windows instances from pre-provisioned snapshots.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner of the Windows AMI for which Windows fast launch was disabled.</p>"""
    state: NotRequired["aws_sdk_ec2.types.fast_launch_state_code.FastLaunchStateCode"]
    """<p>The current state of Windows fast launch for the specified Windows AMI.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason that the state changed for Windows fast launch for the Windows AMI.</p>"""
    state_transition_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that the state changed for Windows fast launch for the Windows AMI.</p>"""
