"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageBlockPublicAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_block_public_access_enabled_state


class EnableImageBlockPublicAccessRequest(TypedDict):
    image_block_public_access_state: NotRequired[
        "aws_sdk_ec2.types.image_block_public_access_enabled_state.ImageBlockPublicAccessEnabledState"
    ]
    """<p>Specify <code>block-new-sharing</code> to enable block public access for AMIs at the account level in the specified Region. This will block any attempt to publicly share your AMIs in the specified Region.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
