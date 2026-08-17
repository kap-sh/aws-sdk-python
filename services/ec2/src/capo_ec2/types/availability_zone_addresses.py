"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_address

AvailabilityZoneAddresses: TypeAlias = list[
    "capo_ec2.types.availability_zone_address.AvailabilityZoneAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneAddresses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.availability_zone_address

        capo_ec2.types.availability_zone_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZoneAddresses:
    import capo_ec2.types.availability_zone_address

    out: AvailabilityZoneAddresses = []
    for child in el.findall("AvailabilityZoneAddress"):
        out.append(
            capo_ec2.types.availability_zone_address.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AvailabilityZoneAddresses:
    import capo_ec2.types.availability_zone_address

    out: AvailabilityZoneAddresses = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.availability_zone_address.deserialize_ec2_query(child)
        )
    return out
