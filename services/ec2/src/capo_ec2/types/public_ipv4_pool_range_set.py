"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolRangeSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.public_ipv4_pool_range

PublicIpv4PoolRangeSet: TypeAlias = list[
    "capo_ec2.types.public_ipv4_pool_range.PublicIpv4PoolRange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolRangeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.public_ipv4_pool_range

        capo_ec2.types.public_ipv4_pool_range.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PublicIpv4PoolRangeSet:
    import capo_ec2.types.public_ipv4_pool_range

    out: PublicIpv4PoolRangeSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.public_ipv4_pool_range.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PublicIpv4PoolRangeSet:
    import capo_ec2.types.public_ipv4_pool_range

    out: PublicIpv4PoolRangeSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.public_ipv4_pool_range.deserialize_ec2_query(child))
    return out
