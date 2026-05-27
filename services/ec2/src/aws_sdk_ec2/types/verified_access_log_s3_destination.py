"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogS3Destination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_delivery_status


class VerifiedAccessLogS3Destination(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_delivery_status.VerifiedAccessLogDeliveryStatus"
    ]
    """<p>The delivery status.</p>"""
    bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket prefix.</p>"""
    bucket_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account number that owns the bucket.</p>"""
