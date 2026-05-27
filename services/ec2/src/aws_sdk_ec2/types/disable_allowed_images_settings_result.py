"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_images_settings_disabled_state


class DisableAllowedImagesSettingsResult(TypedDict):
    allowed_images_settings_state: NotRequired[
        "aws_sdk_ec2.types.allowed_images_settings_disabled_state.AllowedImagesSettingsDisabledState"
    ]
    """<p>Returns <code>disabled</code> if the request succeeds; otherwise, it returns an error.</p>"""
