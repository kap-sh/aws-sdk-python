"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_modification

ReservedInstancesModificationList: TypeAlias = list[
    "capo_ec2.types.reserved_instances_modification.ReservedInstancesModification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesModificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instances_modification

        capo_ec2.types.reserved_instances_modification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesModificationList:
    import capo_ec2.types.reserved_instances_modification

    out: ReservedInstancesModificationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.reserved_instances_modification.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ReservedInstancesModificationList:
    import capo_ec2.types.reserved_instances_modification

    out: ReservedInstancesModificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.reserved_instances_modification.deserialize_ec2_query(child)
        )
    return out
