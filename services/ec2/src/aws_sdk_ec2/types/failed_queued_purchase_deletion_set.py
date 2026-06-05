"""Generated from Smithy shape ``com.amazonaws.ec2#FailedQueuedPurchaseDeletionSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.failed_queued_purchase_deletion

FailedQueuedPurchaseDeletionSet: TypeAlias = list[
    "aws_sdk_ec2.types.failed_queued_purchase_deletion.FailedQueuedPurchaseDeletion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedQueuedPurchaseDeletionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.failed_queued_purchase_deletion

        aws_sdk_ec2.types.failed_queued_purchase_deletion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> FailedQueuedPurchaseDeletionSet:
    import aws_sdk_ec2.types.failed_queued_purchase_deletion

    out: FailedQueuedPurchaseDeletionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.failed_queued_purchase_deletion.deserialize_ec2_query(
                child
            )
        )
    return out
