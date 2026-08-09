"""Generated from Smithy shape ``com.amazonaws.ec2#IpamSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam

IpamSet: TypeAlias = list["capo_ec2.types.ipam.Ipam"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam

        capo_ec2.types.ipam.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> IpamSet:
    import capo_ec2.types.ipam

    out: IpamSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamSet:
    import capo_ec2.types.ipam

    out: IpamSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam.deserialize_ec2_query(child))
    return out
