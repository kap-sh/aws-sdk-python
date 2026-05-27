"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedPrincipal``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.principal_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class AllowedPrincipal(TypedDict):
    principal_type: NotRequired["aws_sdk_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""
