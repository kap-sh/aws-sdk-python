"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_block_public_access_enabled_state


class EnableImageBlockPublicAccessResult(TypedDict):
    image_block_public_access_state: NotRequired[
        "aws_sdk_ec2.types.image_block_public_access_enabled_state.ImageBlockPublicAccessEnabledState"
    ]
    """<p>Returns <code>block-new-sharing</code> if the request succeeds; otherwise, it returns an error.</p>"""
