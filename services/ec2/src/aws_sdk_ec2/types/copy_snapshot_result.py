"""Generated from Smithy shape ``com.amazonaws.ec2#CopySnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CopySnapshotResult(TypedDict):
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the new snapshot.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the new snapshot.</p>"""
