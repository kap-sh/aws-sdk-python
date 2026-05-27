"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTagNotificationAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_tag_key_set


class InstanceTagNotificationAttribute(TypedDict):
    instance_tag_keys: NotRequired[
        "aws_sdk_ec2.types.instance_tag_key_set.InstanceTagKeySet"
    ]
    """<p>The registered tag keys.</p>"""
    include_all_tags_of_instance: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates wheter all tag keys in the current Region are registered to appear in scheduled event notifications. <code>true</code> indicates that all tag keys in the current Region are registered.</p>"""
