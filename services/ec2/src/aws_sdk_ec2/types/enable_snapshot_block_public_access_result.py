"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_block_public_access_state


class EnableSnapshotBlockPublicAccessResult(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The state of block public access for snapshots for the account and Region. Returns either <code>block-all-sharing</code> or <code>block-new-sharing</code> if the request succeeds.</p>"""
