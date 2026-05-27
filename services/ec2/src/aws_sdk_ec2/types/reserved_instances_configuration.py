"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scope
    import aws_sdk_ec2.types.string


class ReservedInstancesConfiguration(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the modified Reserved Instances.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of modified Reserved Instances.</p> <note> <p>This is a required field for a request.</p> </note>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type for the modified Reserved Instances.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network platform of the modified Reserved Instances.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.scope.scope"]
    """<p>Whether the Reserved Instance is applied to instances in a Region or instances in a specific Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
