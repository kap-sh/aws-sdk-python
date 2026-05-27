"""Generated from Smithy shape ``com.amazonaws.ec2#OperatorResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class OperatorResponse(TypedDict):
    managed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the resource is managed by a service provider.</p>"""
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If <code>managed</code> is <code>true</code>, then the principal is returned. The principal is the service provider that manages the resource.</p>"""
    hidden_by_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the resource is hidden by default based on the managed resource visibility settings for the account.</p>"""
