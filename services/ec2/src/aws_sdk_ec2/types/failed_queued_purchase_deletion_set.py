"""Generated from Smithy shape ``com.amazonaws.ec2#FailedQueuedPurchaseDeletionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.failed_queued_purchase_deletion

FailedQueuedPurchaseDeletionSet: TypeAlias = list[
    "aws_sdk_ec2.types.failed_queued_purchase_deletion.FailedQueuedPurchaseDeletion"
]
