"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulQueuedPurchaseDeletionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.successful_queued_purchase_deletion

SuccessfulQueuedPurchaseDeletionSet: TypeAlias = list[
    "capo_ec2.types.successful_queued_purchase_deletion.SuccessfulQueuedPurchaseDeletion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SuccessfulQueuedPurchaseDeletionSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.successful_queued_purchase_deletion

        capo_ec2.types.successful_queued_purchase_deletion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SuccessfulQueuedPurchaseDeletionSet:
    import capo_ec2.types.successful_queued_purchase_deletion

    out: SuccessfulQueuedPurchaseDeletionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.successful_queued_purchase_deletion.deserialize_ec2_query(
                child
            )
        )
    return out
