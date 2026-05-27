"""Generated from Smithy shape ``com.amazonaws.ec2#AddedPrincipal``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.principal_type
    import aws_sdk_ec2.types.string


class AddedPrincipal(TypedDict):
    principal_type: NotRequired["aws_sdk_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""
