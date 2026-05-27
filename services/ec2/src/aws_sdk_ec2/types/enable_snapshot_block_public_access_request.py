"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_block_public_access_state


class EnableSnapshotBlockPublicAccessRequest(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.snapshot_block_public_access_state.SnapshotBlockPublicAccessState"
    ]
    """<p>The mode in which to enable block public access for snapshots for the Region. Specify one of the following values:</p> <ul> <li> <p> <code>block-all-sharing</code> - Prevents all public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. Additionally, snapshots that are already publicly shared are treated as private and they are no longer publicly available.</p> </li> <li> <p> <code>block-new-sharing</code> - Prevents only new public sharing of snapshots in the Region. Users in the account will no longer be able to request new public sharing. However, snapshots that are already publicly shared, remain publicly available.</p> </li> </ul> <p> <code>unblocked</code> is not a valid value for <b>EnableSnapshotBlockPublicAccess</b>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
