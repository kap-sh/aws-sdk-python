"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastLaunchResult``."""

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


class EnableFastLaunchResult(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The image ID that identifies the AMI for which Windows fast launch was enabled.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.fast_launch_resource_type.FastLaunchResourceType"
    ]
    """<p>The type of resource that was defined for pre-provisioning the AMI for Windows fast launch.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.FastLaunchSnapshotConfigurationResponse"
    ]
    """<p>Settings to create and manage the pre-provisioned snapshots that Amazon EC2 uses for faster launches from the Windows AMI. This property is returned when the associated <code>resourceType</code> is <code>snapshot</code>.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_response.FastLaunchLaunchTemplateSpecificationResponse"
    ]
    """<p>The launch template that is used when launching Windows instances from pre-provisioned snapshots.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner ID for the AMI for which Windows fast launch was enabled.</p>"""
    state: NotRequired["aws_sdk_ec2.types.fast_launch_state_code.FastLaunchStateCode"]
    """<p>The current state of Windows fast launch for the specified AMI.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason that the state changed for Windows fast launch for the AMI.</p>"""
    state_transition_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that the state changed for Windows fast launch for the AMI.</p>"""
