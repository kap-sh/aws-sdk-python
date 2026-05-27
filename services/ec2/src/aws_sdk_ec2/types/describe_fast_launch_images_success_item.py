"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesSuccessItem``."""

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


class DescribeFastLaunchImagesSuccessItem(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The image ID that identifies the Windows fast launch enabled image.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.fast_launch_resource_type.FastLaunchResourceType"
    ]
    """<p>The resource type that Amazon EC2 uses for pre-provisioning the Windows AMI. Supported values include: <code>snapshot</code>.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.FastLaunchSnapshotConfigurationResponse"
    ]
    """<p>A group of parameters that are used for pre-provisioning the associated Windows AMI using snapshots.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_response.FastLaunchLaunchTemplateSpecificationResponse"
    ]
    """<p>The launch template that the Windows fast launch enabled AMI uses when it launches Windows instances from pre-provisioned snapshots.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner ID for the Windows fast launch enabled AMI.</p>"""
    state: NotRequired["aws_sdk_ec2.types.fast_launch_state_code.FastLaunchStateCode"]
    """<p>The current state of Windows fast launch for the specified Windows AMI.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason that Windows fast launch for the AMI changed to the current state.</p>"""
    state_transition_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that Windows fast launch for the AMI changed to the current state.</p>"""
