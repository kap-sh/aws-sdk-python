"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogKinesisDataFirehoseDestination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_delivery_status


class VerifiedAccessLogKinesisDataFirehoseDestination(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_delivery_status.VerifiedAccessLogDeliveryStatus"
    ]
    """<p>The delivery status.</p>"""
    delivery_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the delivery stream.</p>"""
