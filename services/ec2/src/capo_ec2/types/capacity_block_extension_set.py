"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtensionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_extension

CapacityBlockExtensionSet: TypeAlias = list[
    "capo_ec2.types.capacity_block_extension.CapacityBlockExtension"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockExtensionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_block_extension

        capo_ec2.types.capacity_block_extension.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityBlockExtensionSet:
    import capo_ec2.types.capacity_block_extension

    out: CapacityBlockExtensionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.capacity_block_extension.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CapacityBlockExtensionSet:
    import capo_ec2.types.capacity_block_extension

    out: CapacityBlockExtensionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.capacity_block_extension.deserialize_ec2_query(child))
    return out
