"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceImageMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_metadata
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.instance_state
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class InstanceImageMetadata(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    launch_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time the instance was launched.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the instance.</p>"""
    zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone of the instance.</p>"""
    state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the instance.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the instance.</p>"""
    image_metadata: NotRequired["aws_sdk_ec2.types.image_metadata.ImageMetadata"]
    """<p>Information about the AMI used to launch the instance.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the instance.</p>"""
