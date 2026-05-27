"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageBlockPublicAccessStateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.string


class GetImageBlockPublicAccessStateResult(TypedDict):
    image_block_public_access_state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of block public access for AMIs at the account level in the specified Amazon Web Services Region.</p> <p>Possible values:</p> <ul> <li> <p> <code>block-new-sharing</code> - Any attempt to publicly share your AMIs in the specified Region is blocked.</p> </li> <li> <p> <code>unblocked</code> - Your AMIs in the specified Region can be publicly shared.</p> </li> </ul>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the state for block public access for AMIs. Possible values include:</p> <ul> <li> <p> <code>account</code> - The state is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The state is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
