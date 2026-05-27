"""Generated from Smithy shape ``com.amazonaws.ec2#FailedQueuedPurchaseDeletion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_queued_reserved_instances_error
    import aws_sdk_ec2.types.string


class FailedQueuedPurchaseDeletion(TypedDict):
    error: NotRequired[
        "aws_sdk_ec2.types.delete_queued_reserved_instances_error.DeleteQueuedReservedInstancesError"
    ]
    """<p>The error.</p>"""
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
