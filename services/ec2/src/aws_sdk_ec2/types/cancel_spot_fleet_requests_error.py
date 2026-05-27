"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_batch_error_code
    import aws_sdk_ec2.types.string


class CancelSpotFleetRequestsError(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.cancel_batch_error_code.CancelBatchErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the error code.</p>"""
