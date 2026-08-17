"""Generated from Smithy shape ``com.amazonaws.ec2#FailedQueuedPurchaseDeletionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.failed_queued_purchase_deletion

FailedQueuedPurchaseDeletionSet: TypeAlias = list[
    "capo_ec2.types.failed_queued_purchase_deletion.FailedQueuedPurchaseDeletion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedQueuedPurchaseDeletionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.failed_queued_purchase_deletion

        capo_ec2.types.failed_queued_purchase_deletion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FailedQueuedPurchaseDeletionSet:
    import capo_ec2.types.failed_queued_purchase_deletion

    out: FailedQueuedPurchaseDeletionSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.failed_queued_purchase_deletion.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FailedQueuedPurchaseDeletionSet:
    import capo_ec2.types.failed_queued_purchase_deletion

    out: FailedQueuedPurchaseDeletionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.failed_queued_purchase_deletion.deserialize_ec2_query(child)
        )
    return out
