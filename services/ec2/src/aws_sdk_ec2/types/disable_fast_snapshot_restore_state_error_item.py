"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreStateErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_state_error
    import aws_sdk_ec2.types.string


class DisableFastSnapshotRestoreStateErrorItem(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    error: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_state_error.DisableFastSnapshotRestoreStateError"
    ]
    """<p>The error.</p>"""
