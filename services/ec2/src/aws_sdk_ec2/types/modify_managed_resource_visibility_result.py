"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedResourceVisibilityResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_resource_visibility_settings


class ModifyManagedResourceVisibilityResult(TypedDict):
    visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_visibility_settings.ManagedResourceVisibilitySettings"
    ]
    """<p>The updated managed resource visibility settings for the account.</p>"""
