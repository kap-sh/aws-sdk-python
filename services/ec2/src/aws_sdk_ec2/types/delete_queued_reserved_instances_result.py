"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteQueuedReservedInstancesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "successful_queued_purchase_deletions" in value:
        import aws_sdk_ec2.types.successful_queued_purchase_deletion_set

        aws_sdk_ec2.types.successful_queued_purchase_deletion_set.serialize_ec2_query(
            value["successful_queued_purchase_deletions"],
            pairs,
            f"{prefix}.SuccessfulQueuedPurchaseDeletionSet",
        )
    if "failed_queued_purchase_deletions" in value:
        import aws_sdk_ec2.types.failed_queued_purchase_deletion_set

        aws_sdk_ec2.types.failed_queued_purchase_deletion_set.serialize_ec2_query(
            value["failed_queued_purchase_deletions"],
            pairs,
            f"{prefix}.FailedQueuedPurchaseDeletionSet",
        )


def deserialize_ec2_query(el: Element) -> DeleteQueuedReservedInstancesResult:
    out: DeleteQueuedReservedInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulQueuedPurchaseDeletionSet") is not None:
        import aws_sdk_ec2.types.successful_queued_purchase_deletion_set

        out["successful_queued_purchase_deletions"] = (
            aws_sdk_ec2.types.successful_queued_purchase_deletion_set.deserialize_ec2_query(
                el, "SuccessfulQueuedPurchaseDeletionSet"
            )
        )
    if el.find("FailedQueuedPurchaseDeletionSet") is not None:
        import aws_sdk_ec2.types.failed_queued_purchase_deletion_set

        out["failed_queued_purchase_deletions"] = (
            aws_sdk_ec2.types.failed_queued_purchase_deletion_set.deserialize_ec2_query(
                el, "FailedQueuedPurchaseDeletionSet"
            )
        )
    return out
