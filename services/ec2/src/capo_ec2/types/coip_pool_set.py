"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_pool

CoipPoolSet: TypeAlias = list["capo_ec2.types.coip_pool.CoipPool"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipPoolSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.coip_pool

        capo_ec2.types.coip_pool.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> CoipPoolSet:
    import capo_ec2.types.coip_pool

    out: CoipPoolSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.coip_pool.deserialize_ec2_query(child))
    return out
