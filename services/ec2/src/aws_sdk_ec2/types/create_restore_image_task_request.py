"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRestoreImageTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_name_request
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateRestoreImageTaskRequest(TypedDict):
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket that contains the stored AMI object.</p>"""
    object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the bucket.</p>"""
    name: NotRequired["aws_sdk_ec2.types.image_name_request.ImageNameRequest"]
    """<p>The name for the restored AMI. The name must be unique for AMIs in the Region for this account. If you do not provide a name, the new AMI gets the same name as the original AMI.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the AMI and snapshots on restoration. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the snapshots, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all of the snapshots that are created.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
