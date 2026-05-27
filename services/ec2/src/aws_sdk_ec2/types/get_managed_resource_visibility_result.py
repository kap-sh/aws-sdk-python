"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedResourceVisibilityResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_resource_visibility_settings


class GetManagedResourceVisibilityResult(TypedDict):
    visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_visibility_settings.ManagedResourceVisibilitySettings"
    ]
    """<p>The managed resource visibility settings for the account.</p>"""
