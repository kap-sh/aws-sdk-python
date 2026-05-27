"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_images_settings_enabled_state


class EnableAllowedImagesSettingsResult(TypedDict):
    allowed_images_settings_state: NotRequired[
        "aws_sdk_ec2.types.allowed_images_settings_enabled_state.AllowedImagesSettingsEnabledState"
    ]
    """<p>Returns <code>enabled</code> or <code>audit-mode</code> if the request succeeds; otherwise, it returns an error.</p>"""
