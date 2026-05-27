"""Generated from Smithy shape ``com.amazonaws.ec2#DisableSnapshotBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_block_public_access_state


class DisableSnapshotBlockPublicAccessResult(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>Returns <code>unblocked</code> if the request succeeds.</p>"""
