"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_state_error_set
    import aws_sdk_ec2.types.string


class DisableFastSnapshotRestoreErrorItem(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    fast_snapshot_restore_state_errors: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_state_error_set.DisableFastSnapshotRestoreStateErrorSet"
    ]
    """<p>The errors.</p>"""
