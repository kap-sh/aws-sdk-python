"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionModifications``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission_list_request


class LoadPermissionModifications(TypedDict):
    add: NotRequired[
        "aws_sdk_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to add.</p>"""
    remove: NotRequired[
        "aws_sdk_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to remove.</p>"""
