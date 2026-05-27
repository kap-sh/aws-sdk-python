"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceImageMetadataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_image_metadata_list
    import aws_sdk_ec2.types.string


class DescribeInstanceImageMetadataResult(TypedDict):
    instance_image_metadata: NotRequired[
        "aws_sdk_ec2.types.instance_image_metadata_list.InstanceImageMetadataList"
    ]
    """<p>Information about the instance and the AMI used to launch the instance.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
