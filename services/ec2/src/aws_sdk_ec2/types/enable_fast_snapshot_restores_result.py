"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_error_set
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_success_set


class EnableFastSnapshotRestoresResult(TypedDict):
    successful: NotRequired[
        "aws_sdk_ec2.types.enable_fast_snapshot_restore_success_set.EnableFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores were successfully enabled.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.enable_fast_snapshot_restore_error_set.EnableFastSnapshotRestoreErrorSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores could not be enabled.</p>"""
