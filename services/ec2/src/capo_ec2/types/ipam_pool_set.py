"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool

IpamPoolSet: TypeAlias = list["capo_ec2.types.ipam_pool.IpamPool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_pool

        capo_ec2.types.ipam_pool.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> IpamPoolSet:
    import capo_ec2.types.ipam_pool

    out: IpamPoolSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam_pool.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamPoolSet:
    import capo_ec2.types.ipam_pool

    out: IpamPoolSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_pool.deserialize_ec2_query(child))
    return out
