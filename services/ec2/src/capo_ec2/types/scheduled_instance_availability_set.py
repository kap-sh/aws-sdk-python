"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceAvailabilitySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instance_availability

ScheduledInstanceAvailabilitySet: TypeAlias = list[
    "capo_ec2.types.scheduled_instance_availability.ScheduledInstanceAvailability"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceAvailabilitySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.scheduled_instance_availability

        capo_ec2.types.scheduled_instance_availability.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ScheduledInstanceAvailabilitySet:
    import capo_ec2.types.scheduled_instance_availability

    out: ScheduledInstanceAvailabilitySet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.scheduled_instance_availability.deserialize_ec2_query(child)
        )
    return out
