"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set
    import aws_sdk_ec2.types.next_token


class DescribeFastSnapshotRestoresResult(TypedDict):
    fast_snapshot_restores: NotRequired[
        "aws_sdk_ec2.types.describe_fast_snapshot_restore_success_set.DescribeFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the state of fast snapshot restores.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
