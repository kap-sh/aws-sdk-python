"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.copy_tags_from_source
    import aws_sdk_ec2.types.instance_specification
    import aws_sdk_ec2.types.snapshot_location_enum
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateSnapshotsRequest(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A description propagated to every snapshot specified by the instance.</p>"""
    instance_specification: NotRequired[
        "aws_sdk_ec2.types.instance_specification.InstanceSpecification"
    ]
    """<p>The instance to specify which volumes should be included in the snapshots.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<note> <p>Only supported for instances on Outposts. If the source instance is not on an Outpost, omit this parameter.</p> </note> <ul> <li> <p>To create the snapshots on the same Outpost as the source instance, specify the ARN of that Outpost. The snapshots must be created on the same Outpost as the instance.</p> </li> <li> <p>To create the snapshots in the parent Region of the Outpost, omit this parameter.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#create-snapshot\"> Create local snapshots from volumes on an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to apply to every snapshot specified by the instance.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    copy_tags_from_source: NotRequired[
        "aws_sdk_ec2.types.copy_tags_from_source.CopyTagsFromSource"
    ]
    """<p>Copies the tags from the specified volume to corresponding snapshot.</p>"""
    location: NotRequired[
        "aws_sdk_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
    ]
    """<note> <p>Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter.</p> </note> <ul> <li> <p>To create local snapshots in the same Local Zone as the source instance, specify <code>local</code>.</p> </li> <li> <p>To create regional snapshots in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default value: <code>regional</code> </p>"""
