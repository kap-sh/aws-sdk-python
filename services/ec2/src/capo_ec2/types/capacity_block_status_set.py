"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_status

CapacityBlockStatusSet: TypeAlias = list[
    "capo_ec2.types.capacity_block_status.CapacityBlockStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_block_status

        capo_ec2.types.capacity_block_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityBlockStatusSet:
    import capo_ec2.types.capacity_block_status

    out: CapacityBlockStatusSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.capacity_block_status.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CapacityBlockStatusSet:
    import capo_ec2.types.capacity_block_status

    out: CapacityBlockStatusSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.capacity_block_status.deserialize_ec2_query(child))
    return out
