"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.failed_queued_purchase_deletion_set
    import aws_sdk_ec2.types.successful_queued_purchase_deletion_set


class DeleteQueuedReservedInstancesResult(TypedDict):
    successful_queued_purchase_deletions: NotRequired[
        "aws_sdk_ec2.types.successful_queued_purchase_deletion_set.SuccessfulQueuedPurchaseDeletionSet"
    ]
    """<p>Information about the queued purchases that were successfully deleted.</p>"""
    failed_queued_purchase_deletions: NotRequired[
        "aws_sdk_ec2.types.failed_queued_purchase_deletion_set.FailedQueuedPurchaseDeletionSet"
    ]
    """<p>Information about the queued purchases that could not be deleted.</p>"""
