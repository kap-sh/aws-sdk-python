"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsInstances``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ids_set
    import aws_sdk_ec2.types.instance_lifecycle
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.launch_template_and_overrides_response
    import aws_sdk_ec2.types.platform_values


class DescribeFleetsInstances(TypedDict):
    launch_template_and_overrides: NotRequired[
        "aws_sdk_ec2.types.launch_template_and_overrides_response.LaunchTemplateAndOverridesResponse"
    ]
    """<p>The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.</p>"""
    lifecycle: NotRequired["aws_sdk_ec2.types.instance_lifecycle.InstanceLifecycle"]
    """<p>Indicates if the instance that was launched is a Spot, On-Demand, Capacity Block, or Interruptible Capacity Reservation instance.</p>"""
    instance_ids: NotRequired["aws_sdk_ec2.types.instance_ids_set.InstanceIdsSet"]
    """<p>The IDs of the instances.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The value is <code>windows</code> for Windows instances in an EC2 Fleet. Otherwise, the value is blank.</p>"""
