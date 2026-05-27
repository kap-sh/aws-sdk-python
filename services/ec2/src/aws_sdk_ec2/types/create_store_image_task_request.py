"""Generated from Smithy shape ``com.amazonaws.ec2#CreateStoreImageTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.s3_object_tag_list
    import aws_sdk_ec2.types.string


class CreateStoreImageTaskRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which the AMI object will be stored. The bucket must be in the Region in which the request is being made. The AMI object appears in the bucket only after the upload task has completed. </p>"""
    s3_object_tags: NotRequired["aws_sdk_ec2.types.s3_object_tag_list.S3ObjectTagList"]
    """<p>The tags to apply to the AMI object that will be stored in the Amazon S3 bucket. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
