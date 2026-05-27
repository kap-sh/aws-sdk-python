"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set


class DisableFastSnapshotRestoresResult(TypedDict):
    successful: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set.DisableFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores were successfully disabled.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set.DisableFastSnapshotRestoreErrorSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores could not be disabled.</p>"""
