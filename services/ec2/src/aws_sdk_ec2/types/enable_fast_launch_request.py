"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastLaunchRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fast_launch_launch_template_specification_request
    import aws_sdk_ec2.types.fast_launch_snapshot_configuration_request
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class EnableFastLaunchRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>Specify the ID of the image for which to enable Windows fast launch.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource to use for pre-provisioning the AMI for Windows fast launch. Supported values include: <code>snapshot</code>, which is the default value.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_request.FastLaunchSnapshotConfigurationRequest"
    ]
    """<p>Configuration settings for creating and managing the snapshots that are used for pre-provisioning the AMI for Windows fast launch. The associated <code>ResourceType</code> must be <code>snapshot</code>.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_request.FastLaunchLaunchTemplateSpecificationRequest"
    ]
    """<p>The launch template to use when launching Windows instances from pre-provisioned snapshots. Launch template parameters can include either the name or ID of the launch template, but not both.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch. Value must be <code>6</code> or greater.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
