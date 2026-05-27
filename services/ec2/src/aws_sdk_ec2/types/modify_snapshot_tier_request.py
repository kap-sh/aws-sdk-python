"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotTierRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.target_storage_tier


class ModifySnapshotTierRequest(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    storage_tier: NotRequired["aws_sdk_ec2.types.target_storage_tier.TargetStorageTier"]
    """<p>The name of the storage tier. You must specify <code>archive</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
