"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instance

ScheduledInstanceSet: TypeAlias = list[
    "capo_ec2.types.scheduled_instance.ScheduledInstance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.scheduled_instance

        capo_ec2.types.scheduled_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ScheduledInstanceSet:
    import capo_ec2.types.scheduled_instance

    out: ScheduledInstanceSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.scheduled_instance.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ScheduledInstanceSet:
    import capo_ec2.types.scheduled_instance

    out: ScheduledInstanceSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.scheduled_instance.deserialize_ec2_query(child))
    return out
