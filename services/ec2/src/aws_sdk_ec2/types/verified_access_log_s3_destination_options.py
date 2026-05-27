"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogS3DestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VerifiedAccessLogS3DestinationOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket prefix.</p>"""
    bucket_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Amazon S3 bucket.</p>"""
