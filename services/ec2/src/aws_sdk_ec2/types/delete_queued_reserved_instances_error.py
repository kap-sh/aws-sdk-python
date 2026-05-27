"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_queued_reserved_instances_error_code
    import aws_sdk_ec2.types.string


class DeleteQueuedReservedInstancesError(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.delete_queued_reserved_instances_error_code.DeleteQueuedReservedInstancesErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message.</p>"""
