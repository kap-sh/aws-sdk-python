"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_message

AvailabilityZoneMessageList: TypeAlias = list[
    "capo_ec2.types.availability_zone_message.AvailabilityZoneMessage"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneMessageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.availability_zone_message

        capo_ec2.types.availability_zone_message.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZoneMessageList:
    import capo_ec2.types.availability_zone_message

    out: AvailabilityZoneMessageList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.availability_zone_message.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AvailabilityZoneMessageList:
    import capo_ec2.types.availability_zone_message

    out: AvailabilityZoneMessageList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.availability_zone_message.deserialize_ec2_query(child)
        )
    return out
