"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointConnectionNotificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ModifyVpcEndpointConnectionNotificationResult(TypedDict):
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, it returns an error.</p>"""
