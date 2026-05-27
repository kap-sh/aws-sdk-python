"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAllowedImagesSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_images_settings_enabled_state
    import aws_sdk_ec2.types.boolean


class EnableAllowedImagesSettingsRequest(TypedDict):
    allowed_images_settings_state: NotRequired[
        "aws_sdk_ec2.types.allowed_images_settings_enabled_state.AllowedImagesSettingsEnabledState"
    ]
    """<p>Specify <code>enabled</code> to apply the image criteria specified by the Allowed AMIs settings. Specify <code>audit-mode</code> so that you can check which AMIs will be allowed or not allowed by the image criteria.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
