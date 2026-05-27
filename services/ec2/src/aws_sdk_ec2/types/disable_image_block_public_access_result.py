"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_block_public_access_disabled_state


class DisableImageBlockPublicAccessResult(TypedDict):
    image_block_public_access_state: NotRequired[
        "aws_sdk_ec2.types.image_block_public_access_disabled_state.ImageBlockPublicAccessDisabledState"
    ]
    """<p>Returns <code>unblocked</code> if the request succeeds; otherwise, it returns an error.</p>"""
