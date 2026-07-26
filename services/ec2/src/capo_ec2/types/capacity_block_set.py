"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block

CapacityBlockSet: TypeAlias = list["capo_ec2.types.capacity_block.CapacityBlock"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_block

        capo_ec2.types.capacity_block.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityBlockSet:
    import capo_ec2.types.capacity_block

    out: CapacityBlockSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.capacity_block.deserialize_ec2_query(child))
    return out
