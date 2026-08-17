"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "capo_ec2.types.availability_zone.AvailabilityZone"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.availability_zone

        capo_ec2.types.availability_zone.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZoneList:
    import capo_ec2.types.availability_zone

    out: AvailabilityZoneList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.availability_zone.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AvailabilityZoneList:
    import capo_ec2.types.availability_zone

    out: AvailabilityZoneList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.availability_zone.deserialize_ec2_query(child))
    return out
