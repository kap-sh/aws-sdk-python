"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogDeliveryStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_delivery_status_code


class VerifiedAccessLogDeliveryStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_delivery_status_code.VerifiedAccessLogDeliveryStatusCode"
    ]
    """<p>The status code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message.</p>"""
