"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_set


class CreateSnapshotsResult(TypedDict):
    snapshots: NotRequired["aws_sdk_ec2.types.snapshot_set.SnapshotSet"]
    """<p>List of snapshots.</p>"""
