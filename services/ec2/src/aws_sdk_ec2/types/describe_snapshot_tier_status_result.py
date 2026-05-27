"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotTierStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_tier_status_set
    import aws_sdk_ec2.types.string


class DescribeSnapshotTierStatusResult(TypedDict):
    snapshot_tier_statuses: NotRequired[
        "aws_sdk_ec2.types.snapshot_tier_status_set.snapshotTierStatusSet"
    ]
    """<p>Information about the snapshot's storage tier.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
