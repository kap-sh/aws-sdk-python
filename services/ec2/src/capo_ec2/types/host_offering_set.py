"""Generated from Smithy shape ``com.amazonaws.ec2#HostOfferingSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.host_offering

HostOfferingSet: TypeAlias = list["capo_ec2.types.host_offering.HostOffering"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostOfferingSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.host_offering

        capo_ec2.types.host_offering.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> HostOfferingSet:
    import capo_ec2.types.host_offering

    out: HostOfferingSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.host_offering.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> HostOfferingSet:
    import capo_ec2.types.host_offering

    out: HostOfferingSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.host_offering.deserialize_ec2_query(child))
    return out
