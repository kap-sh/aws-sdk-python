"""Generated from Smithy shape ``com.amazonaws.ec2#PurchasedScheduledInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instance

PurchasedScheduledInstanceSet: TypeAlias = list[
    "capo_ec2.types.scheduled_instance.ScheduledInstance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchasedScheduledInstanceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.scheduled_instance

        capo_ec2.types.scheduled_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PurchasedScheduledInstanceSet:
    import capo_ec2.types.scheduled_instance

    out: PurchasedScheduledInstanceSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.scheduled_instance.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> PurchasedScheduledInstanceSet:
    import capo_ec2.types.scheduled_instance

    out: PurchasedScheduledInstanceSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.scheduled_instance.deserialize_ec2_query(child))
    return out
