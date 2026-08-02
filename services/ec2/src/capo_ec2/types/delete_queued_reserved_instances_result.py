"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.failed_queued_purchase_deletion_set
    import capo_ec2.types.successful_queued_purchase_deletion_set


class DeleteQueuedReservedInstancesResult(TypedDict, closed=True):
    successful_queued_purchase_deletions: NotRequired[
        "capo_ec2.types.successful_queued_purchase_deletion_set.SuccessfulQueuedPurchaseDeletionSet"
    ]
    """<p>Information about the queued purchases that were successfully deleted.</p>"""
    failed_queued_purchase_deletions: NotRequired[
        "capo_ec2.types.failed_queued_purchase_deletion_set.FailedQueuedPurchaseDeletionSet"
    ]
    """<p>Information about the queued purchases that could not be deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteQueuedReservedInstancesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful_queued_purchase_deletions" in value:
        import capo_ec2.types.successful_queued_purchase_deletion_set

        capo_ec2.types.successful_queued_purchase_deletion_set.serialize_ec2_query(
            value["successful_queued_purchase_deletions"],
            pairs,
            f"{key_prefix}SuccessfulQueuedPurchaseDeletionSet",
        )
    if "failed_queued_purchase_deletions" in value:
        import capo_ec2.types.failed_queued_purchase_deletion_set

        capo_ec2.types.failed_queued_purchase_deletion_set.serialize_ec2_query(
            value["failed_queued_purchase_deletions"],
            pairs,
            f"{key_prefix}FailedQueuedPurchaseDeletionSet",
        )


def deserialize_ec2_query(el: Element) -> DeleteQueuedReservedInstancesResult:
    out: DeleteQueuedReservedInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulQueuedPurchaseDeletionSet") is not None:
        import capo_ec2.types.successful_queued_purchase_deletion_set

        out["successful_queued_purchase_deletions"] = (
            capo_ec2.types.successful_queued_purchase_deletion_set.deserialize_ec2_query(
                el, "SuccessfulQueuedPurchaseDeletionSet"
            )
        )
    if el.find("FailedQueuedPurchaseDeletionSet") is not None:
        import capo_ec2.types.failed_queued_purchase_deletion_set

        out["failed_queued_purchase_deletions"] = (
            capo_ec2.types.failed_queued_purchase_deletion_set.deserialize_ec2_query(
                el, "FailedQueuedPurchaseDeletionSet"
            )
        )
    return out
