"""Generated from Smithy shape ``com.amazonaws.ec2#ResetSnapshotAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_attribute_name
    import aws_sdk_ec2.types.snapshot_id


class ResetSnapshotAttributeRequest(TypedDict):
    attribute: NotRequired[
        "aws_sdk_ec2.types.snapshot_attribute_name.SnapshotAttributeName"
    ]
    """<p>The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
