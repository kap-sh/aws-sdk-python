"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceEventNotificationAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_tag_notification_attribute


class DescribeInstanceEventNotificationAttributesResult(TypedDict):
    instance_tag_attribute: NotRequired[
        "aws_sdk_ec2.types.instance_tag_notification_attribute.InstanceTagNotificationAttribute"
    ]
    """<p>Information about the registered tag keys.</p>"""
