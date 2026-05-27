"""Generated from Smithy shape ``com.amazonaws.ec2#ListSnapshotsInRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_recycle_bin_info_list
    import aws_sdk_ec2.types.string


class ListSnapshotsInRecycleBinResult(TypedDict):
    snapshots: NotRequired[
        "aws_sdk_ec2.types.snapshot_recycle_bin_info_list.SnapshotRecycleBinInfoList"
    ]
    """<p>Information about the snapshots.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
