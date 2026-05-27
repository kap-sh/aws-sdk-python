"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterInstanceEventNotificationAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.register_instance_tag_attribute_request


class RegisterInstanceEventNotificationAttributesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_tag_attribute: NotRequired[
        "aws_sdk_ec2.types.register_instance_tag_attribute_request.RegisterInstanceTagAttributeRequest"
    ]
    """<p>Information about the tag keys to register.</p>"""
