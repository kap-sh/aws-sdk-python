"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set
    import aws_sdk_ec2.types.string


class EnableFastSnapshotRestoreErrorItem(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    fast_snapshot_restore_state_errors: NotRequired[
        "aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set.EnableFastSnapshotRestoreStateErrorSet"
    ]
    """<p>The errors.</p>"""
