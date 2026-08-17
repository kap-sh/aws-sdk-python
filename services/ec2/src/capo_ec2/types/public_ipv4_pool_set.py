"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.public_ipv4_pool

PublicIpv4PoolSet: TypeAlias = list["capo_ec2.types.public_ipv4_pool.PublicIpv4Pool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.public_ipv4_pool

        capo_ec2.types.public_ipv4_pool.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PublicIpv4PoolSet:
    import capo_ec2.types.public_ipv4_pool

    out: PublicIpv4PoolSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.public_ipv4_pool.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PublicIpv4PoolSet:
    import capo_ec2.types.public_ipv4_pool

    out: PublicIpv4PoolSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.public_ipv4_pool.deserialize_ec2_query(child))
    return out
