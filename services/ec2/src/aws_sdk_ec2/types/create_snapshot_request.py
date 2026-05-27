"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_location_enum
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.volume_id


class CreateSnapshotRequest(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the snapshot.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<note> <p>Only supported for volumes on Outposts. If the source volume is not on an Outpost, omit this parameter.</p> </note> <ul> <li> <p>To create the snapshot on the same Outpost as the source volume, specify the ARN of that Outpost. The snapshot must be created on the same Outpost as the volume.</p> </li> <li> <p>To create the snapshot in the parent Region of the Outpost, omit this parameter.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#create-snapshot\">Create local snapshots from volumes on an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the Amazon EBS volume.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the snapshot during creation.</p>"""
    location: NotRequired[
        "aws_sdk_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
    ]
    """<note> <p>Only supported for volumes in Local Zones. If the source volume is not in a Local Zone, omit this parameter.</p> </note> <ul> <li> <p>To create a local snapshot in the same Local Zone as the source volume, specify <code>local</code>.</p> </li> <li> <p>To create a regional snapshot in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default value: <code>regional</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
