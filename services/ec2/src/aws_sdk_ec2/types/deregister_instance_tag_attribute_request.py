"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterInstanceTagAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_tag_key_set


class DeregisterInstanceTagAttributeRequest(TypedDict):
    include_all_tags_of_instance: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to deregister all tag keys in the current Region. Specify <code>false</code> to deregister all tag keys.</p>"""
    instance_tag_keys: NotRequired[
        "aws_sdk_ec2.types.instance_tag_key_set.InstanceTagKeySet"
    ]
    """<p>Information about the tag keys to deregister.</p>"""
