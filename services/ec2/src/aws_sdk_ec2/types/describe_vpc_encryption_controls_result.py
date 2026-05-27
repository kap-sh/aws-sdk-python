"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControlsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_control_list


class DescribeVpcEncryptionControlsResult(TypedDict):
    vpc_encryption_controls: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_list.VpcEncryptionControlList"
    ]
    """<p>Information about the VPC Encryption Control configurations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
